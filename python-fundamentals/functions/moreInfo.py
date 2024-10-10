a: int = 5
a = "str"
print(a)


def sum_nums(a: int, b: int):
    return a + b


print(sum_nums(2, 4))

# Lambdas
nums = [1, 2, 3]

lambda x: x + 5  # anonimous function

print(list(filter(lambda x: x % 2 != 0, nums)))  # find odd numbers


def my_func(*args):
    print(args)


my_func(5, 3, 32, 1, 321, 321, 32)

