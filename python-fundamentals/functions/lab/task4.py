COFFEE = 1.5
WATER = 1
SNACK = 2
COKE = 1.40

prod = input()
quan = int(input())

def calc(prod, quan):
    if prod == 'coffee':
        print( COFFEE*quan)
    elif prod == 'water':
        print(WATER*quan)
    elif prod == "snacks":
        print(SNACK*quan)
    elif prod == 'coke':
        print(COKE*quan)

calc(prod,quan)

