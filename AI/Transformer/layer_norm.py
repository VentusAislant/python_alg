import torch
from torch import nn

class LayerNorm(nn.Module):
    def __init__(self, d_model, eps=1e-6):
        super().__init__()
        self._lambda = nn.Parameter(torch.ones(d_model), requires_grad=True)
        self._beta = nn.Parameter(torch.zeros(d_model), requires_grad=True)
        self.eps = eps

    def forward(self, x):
        """
        x: [bsz, seq_len, d_model]
        """
        mu = torch.mean(x, dim=-1)
        sigma = torch.std(x, dim=-1) + self.eps  # 防止除0错误
        return (x - mu)/sigma * self._lambda + self._beta