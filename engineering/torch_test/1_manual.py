import torch

b = torch.tensor(32)
w1 = torch.tensor(1.8)

X1 = torch.tensor([10.0, 30.0, 50.0, 100.0, 150.0])

y_pred = 1 * b + X1 * w1

print(X1.shape)
print(X1.size())

print(y_pred)

# Access to individual value of  a tensor
print(X1[0])
print(X1[1])
print(X1[2])
print(X1[3])

# Get just the value of a tensor as a Python number
print(X1[0].item())
print(X1[1].item())
print(X1[2].item())
print(X1[3].item())


# Manual

# b = 32
# w1 = 1.8

# X1 = 10

# y_pred = 1 * b + X1 * w1
# print(y_pred)