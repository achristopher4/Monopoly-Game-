# Name: Alexander Christopher
# Email: abc5885@psu.edu
# CMPSC Homework 3


#List for the colors
color = {}
color["purple"] = [2, 50]
color["light blue"] = [3, 50]
color["maroon"] = [3, 100]
color["orange"] = [3, 100] 
color["red"] = [3, 150]
color["yellow"] = [3, 150]
color["green"] = [3, 200]
color["dark blue"] = [2, 200]

#List for number that will be replaced with letters
mathList = {}
mathList[0] = "zero"
mathList[1] = "one"
mathList[2] = "two"
mathList[3] = "three"
mathList[4] = "four"
mathList[5] = "five"
mathList[6] = "six"
mathList[7] = "seven"
mathList[8] = "eight"
mathList[9] = "nine"
mathList[10] = "ten"

#Extra credit HW3
while True:
    askColor = str(input("What color block will you be building on? "))

    if askColor in color:
        break
    elif askColor not in color:
        print("Error: All letters need to be lower case and include a space between words")
    else:
        print("Error: Something went wrong")

#User Input
askMoney = float(input("How much money do you have to spend? "))
askHouses = list(map(int, input("How many houses are already present on these properties? ").split()))

#Algorithm from HW2

#Indexing the dictionary to find the corresponding value with the answer
costIndex = color[askColor][1]
sizeIndex = color[askColor][0]
letterCostIndex = mathList[sizeIndex]

#Making the strings from askHouses into usable integers ready for addition function
#Adding three zeros into the list will be used if 0, 1, or 2 values are typed in
addFirstZero = askHouses.append(0)
addSecondZero = askHouses.append(0)
addThirdZero = askHouses.append(0)

#Indexing the first three values in the askHouses list and adding them together
first = askHouses[0]
second = askHouses[1]
third = askHouses[2]
addStrings = first + second + third 

#Dividing the amount of money by the cost of the house to determine how many houses can be built
amountOfHouses = askMoney // costIndex
letterHousingAmount = mathList[amountOfHouses]

#Extra credit -- Adding the houses already in play with the amount of houses that can be purchased 
totalHousing = addStrings + amountOfHouses

groupTwo = totalHousing % sizeIndex
groupOne = sizeIndex - groupTwo
letterGroupOne = mathList[groupOne]
letterGroupTwo = mathList[groupTwo]


housingOne = totalHousing // sizeIndex
housingTwo = (totalHousing + sizeIndex) // sizeIndex
letterHousingOne = mathList[housingOne]
letterHousingTwo = mathList[housingTwo]

#Alogrithm HW3

if groupOne == 0 and groupTwo == 0:
    print("You cannot afford even one house.")
elif groupTwo == 0 or housingTwo == 0:
    print(f'There are {letterCostIndex} properties and each house costs {costIndex}')
    print(f"You can build {letterHousingAmount} house(s) -- {letterGroupOne} will have {letterHousingOne}")
elif groupOne == 0 or housingOne == 0:
    print(f'There are {letterCostIndex} properties and each house costs {costIndex}')
    print(f"You can build {letterHousingAmount} house(s) -- {letterGroupTwo} will have {letterHousingTwo}")
elif amountOfHouses > 0:
    print(f'There are {letterCostIndex} properties and each house costs {costIndex}')
    print(f"You can build {letterHousingAmount} house(s) -- {letterGroupOne} will have {letterHousingOne} and {letterGroupTwo} will have {letterHousingTwo}")
else:
    print("Error")





