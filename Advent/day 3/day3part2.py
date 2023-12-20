file = open("/Users/dyee25/Desktop/Advent/day 3/day3.txt", "r")

# function to check parts

def checkGear(row, col):
    number = ""
    while table[row][col].isdigit():
        number = number + table[row][col]
        col += 1
        if col >= len(table[row]):
            break
    col -= len(number)
    if (col - 1) >= 0:
        if table[row][col-1] == "*":
            return [int(number), (row, col-1)]
    for i in range(len(number) + 2):
         if (row + 1) < len(table) and (col + i - 1) > 0 and (col + i - 1) < len(table[row]):
             if table[row + 1][col + i - 1] == "*":
                return [int(number), (row + 1,col + i -1)]
    for i in range(len(number) + 2):
         if (row - 1) >= 0 and (col + i - 1) > 0 and (col + i - 1) < len(table[row]):
             if table[row - 1][col + i - 1] == "*":
                return [int(number), (row - 1,col + i -1)]
    col += len(number)
    if (col + 1) <= len(table[row]):
        if table[row][col] == "*":
            return [int(number), (row, col)]
        else:
            return [number, "0", "0"]
    return [number, "0", "0"]

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
gears = []
while row < length:
    while col < width:
        if table[row][col].isdigit():
            number = checkGear(row,col)
            if isinstance(number[0], int):
                #print(number[0])
                col += len(str(number[0]))
            # if the check gear function returned a cordinate, put in in the gears list
            if isinstance(number[1], tuple):
                gears.append(number)
            else:
                col += len(number[0])
        else:
            col += 1
    row += 1
    col = 0
print(gears)
# checks if "part numbers" have the same gear cordinates, then multiplies
for i in range(len(gears)):
    for j in range(len(gears)):
        if gears[i][1] == gears[j][1] and gears[i][0] != gears[j][0]:
            print(gears[i][0], gears[j][0])
            ans += gears[i][0] * gears[j][0]
            gears[i] = [0,(0,0)]

print(ans)
    

