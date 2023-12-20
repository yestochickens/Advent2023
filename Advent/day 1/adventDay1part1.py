file = open("/Users/dyee25/Desktop/Advent/day 1/day1.txt", "r")

number1 = None
number2 = None
stringNumber = 0
finalNumber = 0

for line in file:
    for i in line:
        if i.isnumeric():
            if number1 == None:
                number1 = i
            number2 = i
    
    
    stringNumber = (int(number1) * 10) + int(number2)
    number1 = None
    number2 = None
    finalNumber = finalNumber + stringNumber
    

print(finalNumber)

