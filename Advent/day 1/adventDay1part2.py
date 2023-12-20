file = open("/Users/dyee25/Desktop/Advent/day 1/day1.txt", "r")

number1 = None
number2 = None
stringNumber = 0
finalNumber = 0

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

for line in file:
    i = 1
    for number in numbers:
        if number in line:
            # adds the digit in the middle of the string 
            middleIndex = int(len(number)/2)
            line = line.replace(number, number[0:middleIndex] + str(i) + number[middleIndex:])
        i += 1
    for char in line:
        if char.isnumeric():
            if number1 == None:
                number1 = char
            number2 = char
    
    stringNumber = (int(number1) * 10) + int(number2)
    print(stringNumber)
    number1 = None
    number2 = None
    finalNumber = finalNumber + stringNumber
    

print(finalNumber)
