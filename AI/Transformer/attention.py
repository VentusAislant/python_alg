import torch
from torch import nn
import math

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, n_heads):
        super().__init__()
        assert d_model % n_heads == 0

        self.d_model = d_model
        self.n_heads = n_heads
        self.d_head = d_model // n_heads

        # QKV的映射矩阵, 所有头都拼在一起
        self.Wq = nn.Linear(d_model, d_model, bias=False)
        self.Wk = nn.Linear(d_model, d_model, bias=False)
        self.Wv = nn.Linear(d_model, d_model, bias=False)

        # 输出映射矩阵
        self.Wo = nn.Linear(d_model, d_model, bias=False)

    def forward(self, q, k, v, mask=None):
        """
        q, k, v: [bsz, seq_len, d_model]
        mask: [bsz, 1, 1, seq_len] (padding mask) or [bsz, 1, seq_len, seq_len] (causal mask)
        """
        bsz, seq_len, _ = q.shape

        # 先映射在拆分多头结果和先拆分多头映射矩阵在映射是等价的，前者效率更高
        # 1. 线性映射
        Q = self.Wq(q)  # [bsz, seq_len, d_model]
        K = self.Wk(k)
        V = self.Wv(v)

        # 2. 拆分多头
        Q = Q.view(bsz, seq_len, self.n_heads, self.d_head).transpose(1, 2)  # [bsz, n_heads, seq_len, d_head]
        K = K.view(bsz, seq_len, self.n_heads, self.d_head).transpose(1, 2)
        V = V.view(bsz, seq_len, self.n_heads, self.d_head).transpose(1, 2)

        # 3. Scaled Dot-Product Attention
        scores = torch.matmul(Q, K.transpose(-1, -2)) / math.sqrt(self.d_head)  # [bsz, n_heads, seq_len, seq_len]

        if mask is not None:
            # 将 mask == 0 的位置置为负无穷
            scores = scores.masked_fill(mask == 0, float('-inf'))

        attention = scores.softmax(dim=-1)
        out = torch.matmul(attention, V)  # [bsz, n_heads, seq_len, d_head]

        # 4. 拼接多头注意力结果, 并过输出矩阵
        out = out.transpose(1, 2).contiguous().view(bsz, seq_len, -1)  # [bsz, seq_len, d_model]
        out = self.Wo(out)
        return out

