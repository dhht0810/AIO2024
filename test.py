def function_helper(x, data):
    for _ in data:
        if _ == x:
            return 0
        # Your code here
        # Neu x == i thi return 0
    return 1


def my_function(data):
    res = []
    for i in data:
        if function_helper(i, res):
            res.append(i)
    return res


lst = [10, 10, 9, 7, 7]
assert my_function(lst) == [10, 9, 7]

lst = [9, 9, 8, 1, 1]
print(my_function(lst))
