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
mathList[11] = "eleven"
mathList[12] = "twevle"
mathList[13] = "thirteen"
mathList[14] = "fourteen"
mathList[15] = "fifteen"
mathList[16] = "sixteen"
mathList[17] = "seventeen"
mathList[18] = "eighteen"
mathList[19] = "nineteen"
mathList[20] = "twenty"
mathList[21] = "twenty-one"
mathList[22] = "twenty-two"
mathList[23] = "twenty-three"
mathList[24] = "twenty-four"
mathList[25] = "twenty-five"
mathList[26] = "twenty-six"
mathList[27] = "twenty-seven"
mathList[28] = "twenty-eight"
mathList[29] = "twenty-nine"
mathList[30] = "thrity"


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
finalValueHousing = housingOne + housingTwo

finalValueGrouping = groupOne + groupTwo
letterFinalValueGrouping = mathList[finalValueGrouping]

if (askMoney//costIndex) == 0:
    print("You cannot afford even one house.")
elif groupOne == 0:
    if housingTwo < 5: 
        print(f'You can build {letterHousingAmount} house(s) -- {letterGroupTwo} will have {letterHousingTwo}')
    elif housingTwo <= 5:
        print(f'You can build {letterHousingAmount} house(s) -- {letterGroupTwo} will have a hotel')
    else:
        print("Error: 1")
elif groupTwo == 0:
    if housingOne < 5:
        print(f'You can build {letterHousingAmount} house(s) -- {letterGroupOne} will have {letterHousingOne}')
    elif housingOne <=5:
        print(f'You can build {letterHousingAmount} house(s) -- {letterGroupOne} will have a hotel')
    else:
        print("Error: 2")
elif housingOne == 0:
    if housingTwo < 5: 
        print(f'You can build {letterHousingAmount} house(s) -- {letterGroupTwo} will have {letterHousingTwo}')
    elif housingTwo <= 5:
        print(f'You can build {letterHousingAmount} house(s) -- {letterGroupTwo} will have a hotel')
    else:
        print("Error: 3")
elif housingTwo == 0:
    if housingOne < 5:
        print(f'You can build {letterHousingAmount} house(s) -- {letterGroupOne} will have {letterHousingOne}')
    elif housingOne <=5:
        print(f'You can build {letterHousingAmount} house(s) -- {letterGroupOne} will have a hotel')
    else:
        print("Error: 4")
elif finalValueHousing != 0:
    if housingOne >= 5:
        if housingTwo < 5:
            print(f'You can build {letterHousingAmount} house(s) -- {letterGroupOne} will have a hotel and {letterGroupTwo} will have {letterHousingTwo}')
        elif housingTwo >= 5:
            print(f'{letterFinalValueGrouping} will have a hotel')
        else:
            print("Error: 6")
    elif housingTwo >= 5:
        if housingOne < 5:
            print(f'You can build {letterHousingAmount} house(s) -- {letterGroupOne} will have {letterHousingOne} and {letterGroupTwo} will have a hotel')
        elif housingTwo >= 5:
            print(f'{letterFinalValueGrouping} will have a hotel')
        else:
            print("Error: 7")
    elif finalValueHousing > 0:
        print(f'You can build {letterHousingAmount} house(s) -- {letterGroupOne} will have {letterHousingOne} and {letterGroupTwo} will have {letterHousingTwo}')
    else:
        print("Error: 8")
else:
    print("Error: 9")





