import math


def square(a):
    s = a**2
    return (s)


a = float(input())
result = square(a)
rounded = math.ceil(result)
print(rounded)
