import torch
from torch import nn

X = torch.tensor([
    [10],
    [30],
    [50],
    [100],
], dtype=torch.float32)


model = nn.Linear(in_features=1, out_features=1)
# print(model)

# Manual
model.bias = nn.Parameter(torch.tensor([32.0]))
model.weight = nn.Parameter(torch.tensor([[1.8]]))

print(model.weight)
print(model.bias)

y_pred = model(X)
print(y_pred)
