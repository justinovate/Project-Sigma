import torch
X = torch.tensor([
    [10.0],
    [30.0],
    [50.0],
    [100.0],
])

result = X * 2
print(result)
print(result.dtype)

X = X.type(torch.int64)
print(X)
print(X.dtype)

# print(X.dtype)

# print(X.shape)
# print(X.size(0))
# print(X.size(1))

# print(X[0, 0])
# print(X[1, 0])
# print(X[2, 0])
# print(X[3, 0])

# print(X[:,0])
