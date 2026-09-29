from torch import nn

class FFN(nn.Module):
    def __init__(self, d_model, d_ff=None):
        super().__init__()
        if d_ff is None:
            d_ff = d_model * 4

        self.linear1 = nn.Linear(d_model, d_ff)
        self.activation = nn.ReLU()  # 或者 GELU
        self.linear2 = nn.Linear(d_ff, d_model)

    def forward(self, x):
        return self.linear2(self.activation(self.linear1(x)))