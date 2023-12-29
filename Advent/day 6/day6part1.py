table = []
for line in open("/Users/dyee25/Desktop/Advent/day 6/day6.txt"):
    table.append((line.split(":")[1].split()))


intTable = [[int(x) for x in row] for row in table]
totals = []
for i in range(len(table[0])):
    ans = 0
    totalTime = intTable[0][i]
    record = intTable[1][i]
    for j in range(totalTime + 1):
        holdTime = j
        runTime = totalTime - holdTime
        if (holdTime * runTime) > record:
            ans += 1
    totals.append(ans)
final = 1
for number in totals:
    final *= number
print(final)


