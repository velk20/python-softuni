initEnergy = 100
initCoins = 100

eventList = input().split('|')
end = False

for el in eventList:
    if not end:
        dayEvent = el.split('-')
        event = dayEvent[0]

        match event:
            case "rest":
                energy = int(dayEvent[1])
                if initEnergy + energy > 100:
                    energy = 100 - initEnergy
                    initEnergy = 100
                else:
                    initEnergy+=energy

                print(f"You gained {energy} energy.")
                print(f"Current energy: {initEnergy}.")
                continue
            case "order":
                coins = int(dayEvent[1])
                if initEnergy < 0:
                    initEnergy+=50
                    print("You had to rest!")
                    break
                if initEnergy >= 30:
                    initCoins+=coins
                    print(f"You earned {coins} coins.")
                continue
            case _:
                coins = int(dayEvent[1])

                initCoins -= coins
                if initCoins>0:
                    print(f"You bought {event}.")
                else:
                    print(f"Closed! Cannot afford {event}." )
                    end = True
                continue

if not end:
    print(f"Day completed!")
    print(f"Coins: {initCoins}")
    print(f"Energy: {initEnergy}")