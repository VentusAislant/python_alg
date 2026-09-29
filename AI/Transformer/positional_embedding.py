import torch


class SinusoidalPE:
    """
    正余弦位置编码 Sinusoidal Positional Embedding
        \begin{align}
        & PE_{(pos, 2i)} = sin(\frac{pos}{10000^{\frac{2i}{d}}}) \\
        & PE_{(pos, 2i+1)} = cos(\frac{pos}{10000^{\frac{2i}{d}}}) \\
        \end{align}
    解释：
        - 偶数用 sin, 奇数用 cos
        - 缩放因子  $\frac{1}{10000^{x}}$ 来控制不同维度位置 sin 或 cos 的频率
            - $i$  越小， $\frac{2i}{d}$ 越小， $\frac{1}{10000^x}$ 越大，频率月高
            - 低维 embedding 用高频的 sin/cos， 周期短，适合捕捉短距离局部信息
            - 高维 embedding 用低频的 sin/cos，周期长，适合捕捉长距离全局信息
            - 底部的 10000 是调频参数，让频率在合理范围内分布
                - $\frac{2i}{d} \in [0, 2), \frac{1}{10000^{\frac{2i}{d}}} \in (1e-8, 1]$
    """

    def __init__(self, max_len=1e4, d=4096, device='cpu'):
        """
        args:
            - max_len 表示序列最大长度
            - d 表示模型 embedding 长度
        """
        max_len = int(max_len)
        pe_i = torch.arange(d // 2, device=device, dtype=torch.float32)  # [0, 1, ..., 2047]
        div_term = 10000 ** (2 * pe_i / d)

        # inv_div = 1 / div_term
        # print("min:", inv_div.min().item())
        # print("max:", inv_div.max().item())

        pos = torch.arange(max_len, device=device, dtype=torch.float32).unsqueeze(-1)

        # tmp = pos / div_term
        # print("min:", tmp.min().item())
        # print("max:", tmp.max().item())

        pe_sin = torch.sin(pos / div_term)  # torch.Size([1000000, 2048])
        pe_cos = torch.cos(pos / div_term)

        """
        pe_sin = torch.tensor([[1, 2],      # token 0
                               [5, 6]])     # token 1
        pe_cos = torch.tensor([[10, 20],
                               [50, 60]])
                               
        pe = torch.stack((pe_sin, pe_cos), dim=2)
        tensor([[[ 1, 10],
                 [ 2, 20]],
        
                [[ 5, 50],
                 [ 6, 60]]])  torch.Size([2, 2, 2])
        
        pe = pe.view(2, 4)
        print(pe)
        tensor([[ 1, 10,  2, 20],
                [ 5, 50,  6, 60]])
        """
        pe = torch.stack((pe_sin, pe_cos), dim=2)  # [1000000, 2048, 2]
        self.pe = pe.view(int(max_len), d)  # [1000000, 4096]

    def forward(self, x):
        bsz, len, dim = x.shape
        x += self.pe[:len, :].unsqueeze(0).to(device=x.device, dtype=x.dtype)
        return x

    def visualize(self):
        import matplotlib.pyplot as plt
        plt.figure(figsize=(12, 6))
        plt.imshow(self.pe, aspect='auto', cmap='RdBu_r')
        plt.colorbar()
        plt.xlabel("Embedding Dimension")
        plt.ylabel("Token Position")
        plt.title("Sinusoidal Positional Encoding Heatmap")
        plt.show()


class RoPE:
    def __init__(self, d, device='cpu'):
        self.d = d
        pe_i = torch.arange(d // 2, device=device, dtype=torch.float32)
        self.freqs = 1.0 / 10000 ** (2 * pe_i / d)

    def apply_rope(self, x):
        """
        x: 可以是注意力的 Q 或 K 矩阵，形状 torch.Size[bsz, l, d]
        """
        bsz, l, d = x.shape

        x1 = x[..., ::2]  # 偶数部分  # [bsz, l, d/2]
        x2 = x[..., 1::2]  # 奇数部分

        pos = torch.arange(l, device=x.device, dtype=torch.float32).unsqueeze(-1)  # [l, 1]
        theta = pos * self.freqs.unsqueeze(0)  # [l, d/2]
        theta = theta.unsqueeze(0)  # [1, l, d/2]

        # RoPE
        x_rot_even = x1 * torch.cos(theta) - x2 * torch.sin(theta)  # [bsz, 100, 256]
        x_rot_odd = x1 * torch.sin(theta) + x2 * torch.cos(theta)

        x = torch.stack([x_rot_even, x_rot_odd], dim=-1).view(bsz, l, d)
        return x


class ALiBi:
    def __init__(self, n_heads, device='cpu'):
        self.slopes = torch.tensor([2 ** (-8.0 * i / n_heads) for i in range(n_heads)])

    def apply_alibi(self, attn_score):
        # attn_score: [bsz, n_heads, l, l]
        bsz, n_heads, l, _ = attn_score.shape
        pos = torch.arange(l, device=attn_score.device, dtype=torch.float32)
        diff = pos.unsqueeze(0) - pos.unsqueeze(1)  # [1, l] - [l, 1]  自动广播
        diff = diff.clamp(max=0)  # 将上三角置为 0  [l, l]
        """
        [[0, 0, 0, 0],
         [-1, 0, 0, 0],
         [-2,-1, 0, 0],
         [-3,-2,-1,0]]
        """
        bias = -diff[None, None, :, :] * self.slopes[None, :, None, None]
        # print(bias.shape)  # torch.Size([1, 8, 50, 50])
        # print((attn_score + bias).shape)  # torch.Size([bsz, 8, 50, 50])
        return attn_score + bias


if __name__ == '__main__':
    # pe = SinusoidalPE(max_len=100, d=512)
    # pe.visualize()

    # pe = RoPE(512)
    # x = pe.apply_rope(torch.randn(1, 100, 512))
    # print(x.shape)

    pe = ALiBi(n_heads=8, device='cuda:0')
    x = pe.apply_alibi(torch.randn(2, 8, 50, 50))
    print(x.shape)
