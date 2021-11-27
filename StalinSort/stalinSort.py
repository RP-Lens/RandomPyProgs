import random


#Get range and amount
r = int(input("Enter range: "))
a = int(input("Enter amount: "))

#Seed random number gen
random.seed(2)

#Create a list to hold numbers
nums = []

#Prepare to print unsorted list
print("Unsorted: ")

#Loop for amount of nums
for i in range(a):
    #Assign a random value to nums[i]
    rnd = random.randint(0, r)
    nums.append(rnd)

    #Print number
    print(str(i) + ": " + str(rnd))

#Commence sortinging
print("Sorted: ")
new = []
j = nums[0]
count = 0

#Find length of nums and check if it is greater than index
for i in range(a):
    #Check if current elemnt >= j
    if nums[i] >= j:
        #Add new number to new array
        new.append(nums[i])
        j = nums[i]
        count += 1

for i in range(count):
    print(str(i) + ": " + str(new[i]))
