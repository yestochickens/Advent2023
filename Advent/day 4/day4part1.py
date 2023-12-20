file = open("/Users/dyee25/Desktop/Advent/day 4/day4.txt", "r")

winners = []
guessed = []
totalNumbers = []
count = 0
ans = 0

for line in file:
    newLine = line.split(" ")
    for x in newLine:
        if x != "":
            totalNumbers.append(x)
    winners = totalNumbers[2:12]
    guessed = totalNumbers[13:]
    guessed[-1] = guessed[-1][:-1]
    for i in range(len(guessed)):
        if guessed[i] in winners:
            print(guessed[i])
            count += 1
            print(count)
    if count > 0:
        ans += 2 ** (count - 1)
    count = 0
    guessed = []
    winners = []
    totalNumbers = []
    print(ans)