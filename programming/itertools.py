from itertools import starmap

def multiply(x: float, y: float):
    return x * y

nums = [(1,2), (4,2), (2,5)]

list(starmap(multiply, nums))