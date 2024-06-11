import math

# Given
def is_number(n) :
    try :
        float (n) # Type - casting the string to ‘float ‘.
    # If string is not a valid ‘float ‘ ,
    # it ’ll raise ‘ValueError ‘ exception
    except ValueError :
        return False
    return True

def sigmoid_function(x):
    return 1 / (1 + math.exp(-x))

def relu_function(x):
     if x <= 0:
         return 0
     return x

def elu_function(x, alpha = 0.1):
    if x <=0 :
        return alpha * (math.exp(x) - 1)
    return x

def main_function():
    supported_functions = ['sigmoid', 'relu', 'elu']
    x = input('Input x = ')
    type_function = input('Input activation Function ( sigmoid | relu | elu ): ')
    if is_number(x) == False:
        return "x must be a number"
    x = float(x)
    
    if type_function.lower() not in supported_functions:
        return type_function + " is not supported"
    if type_function == supported_functions[0]:
        return sigmoid_function(x)
    elif type_function == supported_functions[1]:
        return relu_function(x)
    return elu_function(x)

print(main_function())


