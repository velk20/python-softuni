string = input().split(", ")

def isPalindrome(num):
    reversedNum = num[::-1]
    return  num == reversedNum

for int_value in string:
    print(isPalindrome(int_value))