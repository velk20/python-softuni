ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLANDS = 3
TREE_LIGHTS = 15

quantity = int(input())
days = int(input())

total = 0
spirits = 0

for day in range(1,days+1):
    if day % 11 == 0:
        quantity+=2
    if day % 2 == 0:
        total += quantity*ORNAMENT_SET
        spirits += 5
    if day % 3 == 0:
        total += quantity*TREE_SKIRT
        total += quantity*TREE_GARLANDS
        spirits += 13
    if day % 5 == 0:
        total += quantity*TREE_LIGHTS
        spirits+=17
    if day % 5 == 0 and day % 3 == 0:
        spirits+=30
    if day % 10 == 0:
        spirits -= 20
        total += TREE_SKIRT + TREE_LIGHTS + TREE_GARLANDS
    if day == days and day % 10 == 0:
        spirits -= 30

print(f"Total cost: {total}")
print(f"Total spirit: {spirits}")



