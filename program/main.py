def add_one(value):
    if value == 10:
        return 11
    if value == 11:
        return 12
    if value == 13:
        return 14
    return value + 1

def multiply_by_two(value):
    return value * 2

def my_partial_fn(x):
    y = 0
    if x:
        y = 10
    return y