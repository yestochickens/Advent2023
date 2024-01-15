file = open("/Users/dyee25/Desktop/Advent/day 2/day2.txt", "r")

colors = {"red": 12, "green": 13, "blue": 14}

table = []
i = 0
# puts colors in table and deletes game 1: splits it after each space
for line in file:
    table.append(line.split(" "))
    table[i] = table[i][2:]
    i += 1
rowPrinted = False
total = 0
for i in range(len(table)+1):
    total += i
row = 0
col = 0
for line in table:
    for item in line:
        for color in colors:
            if color in item:
                # if you have more balls that your supposed to the row is added to the total
                if (colors[color] < int(table[row][col-1])) and not(rowPrinted):
                    total -= row+1
                    # makes sure each line is only printed once
                    rowPrinted = True
                    break
        col += 1
    row += 1
    col = 0
    rowPrinted = False
print(total)





