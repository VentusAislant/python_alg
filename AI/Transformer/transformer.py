"""
Transformer 实现，主要模块包含
    Sinusoidal Positional Embedding 正余弦位置编码
    Multi Head Attention 多头注意力
    Layer Normalization 层归一化
    FFN 前馈神经网络
"""
import torch
import math
from torch import nn

class SinusoidalPositionalEmbedding(nn.Module):
    """
    正余弦位置编码类
        x = x + pe
        pe(pos, 2i) = sin( pos / 10000 ** (2i / d) )  偶数用正弦
        pe(pos, 2i+1) = cos( pos / 10000 ** (2i / d) )  奇数用余弦
    """
    def __init__(self, d_model, max_len, device='cpu'):
        super().__init__()
        assert d_model % 2 == 0
        pe_i = torch.arange(d_model // 2, device=device, dtype=torch.float32)
        div_term = 10000 ** (2 * pe_i / d_model)  # [d_model/2]
        pos = torch.arange(max_len, device=device, dtype=torch.float32)
        pe_sin = torch.sin(pos[:, None] / div_term[None,:])  # [max_len, d_model/2]
        pe_cos = torch.cos(pos[:, None] / div_term[None,:])
        # 交错
        self.pe =  torch.stack([pe_sin, pe_cos], dim=-1).view(max_len, d_model)

    def forward(self, x):
        # x: [bsz, seq_len, d_model]
        seq_len = x.size(1)
        return x + self.pe[None, :seq_len, :]


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads, device='cpu'):
        """
        d_model: 模型的维度
        num_heads: 头的数量
        默认 Q,K,V 的输入维度都是 d_model
        """
        super().__init__()
        assert d_model % num_heads == 0

        self.num_heads = num_heads
        self.d_model = d_model
        self.d_head = d_model // num_heads

        self.Wq = nn.Linear(d_model, d_model, bias=False, device=device)
        self.Wk = nn.Linear(d_model, d_model, bias=False, device=device)
        self.Wv = nn.Linear(d_model, d_model, bias=False, device=device)

        self.Wo = nn.Linear(d_model, d_model, bias=False, device=device)


    def forward(self, q, k, v, mask=None):
        """
        qkv: [bsz, seq_len, d_model]
        mask: [bsz, 1, 1, seq_len] (padding mask) or [bsz, 1, seq_len, seq_len] (causal mask)
        """
        bsz, q_len, _ = q.shape
        _, k_len, _ = k.shape

        # 1. 线性映射
        Q = self.Wq(q)  # [bsz, seq_len, d_model]
        K = self.Wk(k)
        V = self.Wv(v)

        # 2. 拆分多头
        Q = Q.view(bsz, q_len, self.num_heads, self.d_head).transpose(1, 2)  # [bsz, num_heads, seq_len, d_head]
        K = K.view(bsz, k_len, self.num_heads, self.d_head).transpose(1, 2)
        V = V.view(bsz, k_len, self.num_heads, self.d_head).transpose(1, 2)

        # 3. scaled dot-product attention
        score = torch.matmul(Q, K.transpose(-1, -2)) / math.sqrt(self.d_head)

        if mask is not None:
            score = score.masked_fill(mask == 0, float('-inf'))

        attention = torch.softmax(score, dim=-1)
        out = torch.matmul(attention, V)

        # 4. 合并多头并输出矩阵映射
        out = out.transpose(1, 2).contiguous().view(bsz, q_len, -1)
        out = self.Wo(out)
        return out


class LayerNorm(nn.Module):
    def __init__(self, d_model, eps=1e-6, device='cpu'):
        super().__init__()
        self._lambda = nn.Parameter(torch.ones(d_model).to(device), requires_grad=True)
        self._beta = nn.Parameter(torch.zeros(d_model).to(device), requires_grad=True)
        self.eps = eps

    def forward(self, x):
        # x: [bsz, seq_len, d_model]
        mu = torch.mean(x, dim=-1, keepdim=True)  # [bsz, seq_len, 1]
        # 不是统计估计问题，不需要做无偏修正，只是仅仅计算特征维度的标准差
        sigma = torch.std(x, dim=-1, keepdim=True, unbiased=False) + self.eps # [bsz, seq_len, 1]
        x_hat = (x - mu) / sigma
        return x_hat * self._lambda[None, None,:] + self._beta[None, None,:]  # [bsz, seq_len, d_model]

class FFN(nn.Module):
    def __init__(self, d_model, d_ff=None, device='cpu'):
        super().__init__()
        if d_ff is None:
            d_ff = d_model * 4

        self.d_ff = d_ff
        self.d_model = d_model
        self.linear1 = nn.Linear(d_model, d_ff, device=device)
        self.activation = nn.ReLU() # 或 GELU
        self.linear2 = nn.Linear(d_ff, d_model, device=device)

    def forward(self, x):
        # x: [bsz, seq_len, d_model]
        return self.linear2(self.activation(self.linear1(x)))

class TransformerEncoderLayer(nn.Module):
    def __init__(self, d_model, d_ff, num_heads, device='cpu'):
        super().__init__()
        self.mha = MultiHeadAttention(d_model, num_heads, device)
        self.ffn = FFN(d_model, d_ff, device)
        self.ln1 = LayerNorm(d_model, device=device)
        self.ln2 = LayerNorm(d_model, device=device)

    def forward(self, x, mask=None):
        """
        x: [bsz, seq_len, d_model]
        mask: [bsz, 1, 1, seq_len]
        """
        x1 = self.mha(x, x, x, mask)
        x2 = self.ln1(x1 + x)
        x3 = self.ffn(x2)
        x4 = self.ln2(x2 + x3)  # [bsz, seq_len, d_model]
        return x4

class TransformerDecoderLayer(nn.Module):
    def __init__(self, d_model, d_ff, num_heads, device='cpu'):
        super().__init__()
        # Masked Multi Head Attention
        self.mmha = MultiHeadAttention(d_model, num_heads, device)
        self.mha = MultiHeadAttention(d_model, num_heads, device)
        self.ffn = FFN(d_model, d_ff, device)
        self.ln1 = LayerNorm(d_model, device=device)
        self.ln2 = LayerNorm(d_model, device=device)
        self.ln3 = LayerNorm(d_model, device=device)

    def construct_causal_mask(self, mask, bsz, seq_len, device):
        """
            根据传入的 mask [bsz, 1, 1, seq_len] or None
            构建 causal mask  [bsz, 1, seq_len, seq_len]
        """
        # 下三角矩阵，其余位置为 0
        causal_mask = torch.tril(torch.ones(seq_len, seq_len, device=device)) # [seq_len, seq_len]
        causal_mask = causal_mask[None, None, :, :]  # [1, 1, seq_len, seq_len]
        causal_mask = causal_mask.expand(bsz, 1, seq_len, seq_len)  # [bsz, 1, seq_len, seq_len]
        if mask is not None:
            causal_mask = causal_mask * mask.float()
        return causal_mask

    def forward(self, x, encoder_output, mask=None, encoder_mask=None):
        """
        x: [bsz, seq_len, d_model]
        encoder_output: [bsz, seq_len, d_model]
        mask: [bsz, 1, 1, seq_len] | None
        """
        bsz, seq_len, _ = x.shape
        causal_mask = self.construct_causal_mask(mask, bsz, seq_len, x.device)

        x1 = self.mmha(x, x, x, causal_mask)
        x2 = self.ln1(x1 + x)

        # 这里需要屏蔽 decoder 的嵌入 去看  encoder 嵌入中的 padding 的位置
        x3 = self.mha(x2, encoder_output, encoder_output, encoder_mask)
        x4 = self.ln2(x2 + x3)

        x5 = self.ffn(x4)
        x6 = self.ln3(x4 + x5)
        return x6


class Transformer(nn.Module):
    def __init__(
            self,
            num_encoder_layers,
            num_decoder_layers,
            vocab_size,
            d_model,
            num_heads,
            d_ff=None,
            max_seq_len=10000,
            device='cpu'
    ):
        super().__init__()
        self.input_embedding = nn.Embedding(vocab_size, d_model)
        self.positional_encoding = SinusoidalPositionalEmbedding(d_model, max_seq_len, device=device)
        self.encoder = nn.ModuleList([
            TransformerEncoderLayer(d_model, d_ff, num_heads, device) for _ in range(num_encoder_layers)
        ])
        self.decoder = nn.ModuleList([
            TransformerDecoderLayer(d_model, d_ff, num_heads, device) for _ in range(num_decoder_layers)
        ])
        self.head = nn.Linear(d_model, vocab_size, bias=False)
        self.head.weight = self.input_embedding.weight  # 绑定输入和输出转换矩阵的权重

    def forward(self, encoder_input_ids, decoder_input_ids, encoder_mask, decoder_mask):
        """
        encoder_inputs: [bsz, seq_len]
        decoder_inputs: [bsz, seq_len_out]
        encoder_mask: [bsz, 1, 1, seq_len]
        decoder_mask: [bsz, 1, 1, seq_len_out]
        """
        # 编码阶段
        encoder_input_embedding = self.input_embedding(encoder_input_ids)  # [bsz, seq_len, d_model]
        encoder_input_embedding = self.positional_encoding(encoder_input_embedding) # [bsz, seq_len, d_model]
        encoder_output = encoder_input_embedding
        for encoder_layer in self.encoder:
            encoder_output = encoder_layer(encoder_output, encoder_mask)

        # 解码阶段
        decoder_input_embedding = self.input_embedding(decoder_input_ids) # [bsz, seq_len, d_model]
        decoder_input_embedding = self.positional_encoding(decoder_input_embedding) # [bsz, seq_len, d_model]
        decoder_output = decoder_input_embedding
        for decoder_layer in self.decoder:
            decoder_output = decoder_layer(decoder_output, encoder_output, decoder_mask, encoder_mask)

        # 输出
        logits = self.head(decoder_output)
        return logits

    @torch.no_grad()
    def generate(self, encoder_input_ids, max_gen_len, decoder_start_token_id, decoder_end_token_id):
        """
        自回归生成, 非批次生成
            encoder_input_ids: [seq_len]
            max_gen_len: 最大生成长度
            decoder_start_token_id: 解码器序列起始 token id
            decoder_end_token_id: 解码器序列结束 token id
        """
        device = encoder_input_ids.device  # [1, seq_len]
        encoder_input_ids = encoder_input_ids.unsqueeze(0)
        decoder_input_ids = torch.ones((1, 1), device=device, dtype=torch.long) * decoder_start_token_id

        res = [decoder_start_token_id]
        for _ in range(max_gen_len):
            logits = self.forward(
                encoder_input_ids=encoder_input_ids,
                decoder_input_ids=decoder_input_ids,
                encoder_mask=None,
                decoder_mask=None,
            )  # [1, seq_len, vocab_size]
            out_token = torch.argmax(logits[:, -1, :], dim=-1).item()  # 只拿出最后一个 token
            res.append(out_token)
            if out_token == decoder_end_token_id:
                break

            # 拼接新的 token
            next_token_tensor = torch.tensor([[out_token]], device=device, dtype=torch.long)
            decoder_input_ids = torch.cat([decoder_input_ids, next_token_tensor], dim=1)
        return torch.tensor(res)

