import torch
from torch import nn

# Prepare our Input Data
# X1 = torch.tensor([10.0], dtype=torch.float32)
# Y1 = torch.tensor([50.0], dtype=torch.float32)

# X2 = torch.tensor([37.78], dtype=torch.float32)
# Y2 = torch.tensor([100.0], dtype=torch.float32)

X_batch = torch.tensor([[10], [37.78]], dtype=torch.float32)
Y_batch = torch.tensor([[50], [100]], dtype=torch.float32)


# Prepare for the Training
model = nn.Linear(in_features=1, out_features=1)
loss_fn = nn.MSELoss()

# for i in model.parameters():
#     print(i)

# print(loss_fn(
#     torch.tensor([5.5]),
#     torch.tensor([50.0])
# ))

optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)

# print(f"Initial Weights before the Training Pass")
# print(f"{model.bias}")
# print(f"{model.weight}")

for i in range(1, 150000):
    optimizer.zero_grad()
    outputs = model(X_batch)
    loss = loss_fn(outputs, Y_batch)
    loss.backward()
    optimizer.step()

    if i % 100 == 0:
        print(f"Weight: {model.weight}")
        print(f"Bias: {model.bias}\n")

measurements = torch.tensor([[20.0], [40.0]], dtype=torch.float32)
model.eval()
with torch.no_grad():
    predictions = model(measurements)
    print(predictions)

# Training Pass
# Forward Pass, Loss Calculation, Backward Pass, and Parameter Update

# Step 1: Zero the Gradients
# optimizer.zero_grad()

# Step 2: Forward Pass
# y_pred = model(X1)

# Step 3: Loss Calculation
# loss = loss_fn(y_pred, Y1)
# print(f"Loss: {loss}")

# Step 4: Backward Pass
# loss.backward()

# Step 5: 
# optimizer.step()

# print(f"Updated Weights after the Training Pass")
# print(f"{model.bias}")
# print(f"{model.weight}")