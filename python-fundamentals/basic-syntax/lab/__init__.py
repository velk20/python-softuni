a = 23
b = 10
c = 5

###
if a > b:
    print("Yes")
###
if not a==c: # Don't use '!='
    print("Different")
####
if a > b:
    print("Greater")
else:
    print("Lower")
####
if a > b:
    print("if")
elif a < b:
    print("elif")
else:
    print("else")

####
if a > b and b > a:
    print("Correct")
elif a>b or c<b:
    print("Incorrect")

### range
if c < a < 100:
    print("Correct")