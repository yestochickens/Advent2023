file = open("/Users/dyee25/Desktop/Advent/day 4/day4.txt", "r")

winners = []
guessed = []
totalNumbers = []
cardInstances = [1] * 204
lineNumber = 1
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
            count += 1
    for i in range(count):
        cardInstances[lineNumber + i] += cardInstances[lineNumber - 1]
    count = 0
    lineNumber += 1
    guessed = []
    winners = []
    totalNumbers = []
for i in range(len(cardInstances)):
    ans += cardInstances[i]
print(ans)