file = open("/Users/dyee25/Desktop/Advent/day 3/day3.txt", "r")

# function to check parts

def checkPart(row, col):
    number = ""
    while table[row][col].isdigit():
        number = number + table[row][col]
        col += 1
        if col >= len(table[row]):
            break
    col -= len(number)
    if (col - 1) >= 0:
        if table[row][col-1] != "." and table[row][col-1].isdigit() == False:
            return int(number)
    for i in range(len(number) + 2):
         if (row + 1) < len(table) and (col + i - 1) > 0 and (col + i - 1) < len(table[row]):
             if table[row + 1][col + i - 1] != "." and table[row+1][col + i - 1].isdigit() == False:
                 return int(number)
    for i in range(len(number) + 2):
         if (row - 1) >= 0 and (col + i - 1) > 0 and (col + i - 1) < len(table[row]):
             if table[row - 1][col + i - 1] != "." and table[row - 1][col + i - 1].isdigit() == False:
                 return int(number)
    col += len(number)
    if (col + 1) <= len(table[row]):
        if table[row][col] != "." and table[row][col].isdigit() == False:
            return int(number)
        else:
            return number
    return number

# put the data in a table
table = []
for line in file:
    newLine = line.replace("\n", "")
    table.append(newLine)
length = len(table)
width = len(table[0])

# if you find a number add to string number, and keep adding numbers to that string until you reach a ".". 
ans = 0
row = 0
col = 0
while row < length:
    while col < width:
        if table[row][col].isdigit():
            number = checkPart(row,col)
            if isinstance(number, int):
                print(number)
                ans += number
                col += len(str(number))
            else:
                col += len(number)
        else:
            col += 1
    row += 1
    col = 0


print(ans)
    

