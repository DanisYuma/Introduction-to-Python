def sum(x, y):
    return x + y

f = sum

def mylt(x, y):
    return x * y

def calc(op, a, b):
    # return op(a, b)
    print(op(a, b))

calc(mylt, 4, 5)
calc(f, 4, 5)