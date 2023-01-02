# Importing random numbers from library
import random

# Make a function to define list of 3 random values as integers
# Considering 0 -> boy and 1-> girl

# Entering the number of events that should consider
eventsCount = int(input("Enter the No of Events = "))


def findProbability():
    childGender = [random.randint(0, 1) for _ in range(3)]

    # check whether the random values are satisfying the logic
    # 1 child is a girl and all 3 are girls
    atLeast = 1 in childGender
    allGirls = childGender = [1, 1, 1]
    return atLeast and allGirls


# Run the program upto 1000 times and count number of times it satisfy the condition
# Condition is "no. of times at least 1 chid is a girl and all children are girls"
noOfSatisfactions = 0
# eventsCount = 1000
for _ in range(eventsCount):
    if findProbability():
        noOfSatisfactions += 1


probability = noOfSatisfactions/eventsCount

print(" \nNo of Events Checked = ", eventsCount, end="\n")
print("No of times at least one of the children is a girl, all are girls = ",
      noOfSatisfactions, end="\n")
print("The Final Probability is ", probability)
