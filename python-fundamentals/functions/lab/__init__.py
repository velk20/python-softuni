def func(name: str):
    print(name)

func("Angel")


def fun1(name: list, tup: tuple):
    print(name)
    print(tup)

fun1([1,2,3],(1,2,3))

def sumNums(a:int,b:int):
    return a+b

def sumNumsWithDefault(a=5,b=6): # With Default values
    print(a,b)

sumNumsWithDefault(b=12) #chaning only one of the arguments


print(sumNums(1,2))
sumNumsWithDefault()
sumNumsWithDefault(10,11)

def checkIfValueIsPositive(num:int):
    return type(num) == int

print(checkIfValueIsPositive(2))
print(checkIfValueIsPositive(-2))
print(checkIfValueIsPositive("2"))
