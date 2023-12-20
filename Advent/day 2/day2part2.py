file = open("/Users/dyee25/Desktop/Advent/day 2/day2.txt", "r")

colors = {"red": 0, "green": 0, "blue": 0}

table = []
for line in file:
    # puts colors in table and deletes game 1: splits it after each , or ;
    line = line.replace(";", ",")
    line = line.replace(":", ",")
    line_list = line.split(", ")
    line_list = line_list[1:]
    table.append(line_list)

print(table)
total = 0
row = 0
col = 0
for line in table:
    for item in line:
        item = item.replace("\n", "")
        table[row][col] = item
        if table[row][col][2] == " ":
            index = 3
        else:
            index = 2
        # checks if the new input requires less balls
        if colors[table[row][col][index:]] < int(table[row][col][0:index-1]):
            colors[table[row][col][index:]] = int(table[row][col][0:index-1])
        col += 1

    row += 1
    col = 0
    print(colors)
    # multiplies the total
    total += colors["red"] * colors["green"] * colors["blue"]
    colors = {"red": 0, "green": 0, "blue": 0}
    print(total)




