import numbers

num=int(input())

for n in range (num): #exclusive
    print(n)
print("--------------------------")
for n in range (1, num+1, 2): #start num, end num, step for looping
    print(n)

name = "Angel"
for char in name:
    print(char)

number = 4
while(number>0):
    print(number)
    number-=1