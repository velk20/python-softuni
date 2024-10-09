word = ["Hello",213, True, 2.2]

print(word[0])

list_ex = ["apple","banana", "dsad"]
print("-".join(list_ex))

print(list_ex[0])

list_input = list() # creating new empty list
list_input.append("dsa")
print(list_input)

text = "a b c d"
my_list = text.split(" ")
print(my_list)

nums = [1,2,3,4,5,6]
#Iterating elements
for el in nums:
    print(el)
print("---------------")
#Iterating by indexes
for index in range(0,len(nums)):
    print(nums[index], end="-")

#Changeing
nums[0] = 1000
print(nums)

#Swap values in list
market = ["Chips", "Milk", "Tea"]
print("Old: "+",".join(market))

market[0], market[1] = market[1], market[0]
print("Swapped: "+",".join(market))

#Adding
nums.append(123123)
nums.append(321321)
print(nums)

#By index
nums.insert(0,0)
print(nums)

#Remove
nums.remove(321321)
print(nums)

print(any(nums))

#Remove from specific element
nums.pop()
nums.pop(1)

