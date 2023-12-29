def main():

    table = []
    for line in open("/Users/dyee25/Desktop/Advent/day 6/day6.txt"):
        table.append((line.split(":")[1].split()))
    time = ""
    distance = ""
    for i in range(len(table[0])):
        time = time + table[0][i]
    for i in range(len(table[0])):
        distance = distance + table[1][i]

        ans = 0
    for j in range((int)(time) + 1):
        holdTime = j
        runTime = (int)(time) - holdTime
        if (holdTime * runTime) > (int)(distance):
            ans += 1
    print(ans)

main()
