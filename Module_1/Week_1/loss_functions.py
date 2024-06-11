import math
import random

def compute_loss(loss_name):
    target = random.uniform(0, 10)
    pred = random.uniform(0, 10)
    
    if loss_name.upper() == "MAE":
        mae = abs(target - pred)
        return (pred, target, mae)
    elif loss_name.upper() in ["MSE", "RMSE"]:
        mse = (target - pred) ** 2
        return (pred, target, mse)
    else:
        return None  

def compute_error():
    n = int(input('Input number of samples (integer number) which are generated: '))
    loss_name = input('Input loss name: ').upper()
    total_loss = 0
    
    for i in range(n):
        loss = compute_loss(loss_name)
        if loss is None:
            print(f"Unsupported loss function: {loss_name}")
            return
        total_loss += loss[2]
        print(f"loss name: {loss_name}, sample: {i}, pred: {loss[0]}, target: {loss[1]}, cumulative loss: {total_loss}")

    if loss_name == 'MAE':
        total_error = total_loss / n
    elif loss_name == 'MSE':
        total_error = total_loss / n
    elif loss_name == 'RMSE':
        total_error = math.sqrt(total_loss / n)
    else:
        print(f"Unsupported loss function: {loss_name}")
        return

    print(f"Final error ({loss_name}): {total_error}")

print(compute_error())
