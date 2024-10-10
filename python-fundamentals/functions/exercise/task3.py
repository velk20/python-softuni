start = ord(input())
end = ord(input())

def asciInBetween(start, end):
    chars = []

    for i in range(start, end):
        chars.append(chr(i))

    return chars

print(asciInBetween(start+1,end))


