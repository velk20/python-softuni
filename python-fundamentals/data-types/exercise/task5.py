start = int(input())
end = int(input())

out = ''

while start<=end:
    out+=chr(start)
    start+=1

print(out)