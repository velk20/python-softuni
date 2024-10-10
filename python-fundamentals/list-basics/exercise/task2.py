a=int(input())
b=int(input())

tempA=a

list=[]
for _ in range(b):
    list.append(tempA)
    tempA+=a

print(list)