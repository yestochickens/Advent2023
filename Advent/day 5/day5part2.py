def main():
    file = open("/Users/dyee25/Desktop/Advent/day 5/day5.txt", "r")
    table = []
    # makes the seed array
    for line in file:
        newLine = line.split("\n")
        newNewLine = newLine[0].split(" ")
        table.append(newNewLine)
    mapValues = [[] for _ in range(7)]
    index = 0
    for i in range(len(table)):
        if len(table[i]) == 2:
            i += 1 
            while len(table[i]) == 3: 
                mapValues[index].append(table[i])
                i += 1
                if i >= len(table):
                    break
            index += 1
    # makes array into ints
    intMapValues = [
        [
        [int(num) for num in array] for array in table
        ]
        for table in mapValues
    ]
    dees = [int(i) for i in (table[0][1:])]
    seeds = []
    # finds the intervals to test
    for i in range(0, len(dees), 2):
        seeds.append((dees[i], dees[i] + dees[i+1]))
    for i in range(len(intMapValues)):
        newValues = []
        while len(seeds) > 0:
            start, end = seeds.pop()
            for endMap, startMap, rangeMap in intMapValues[i]:
                # finds where seeds overlaps with soil
                overlapStart = max(start, startMap)
                overlapEnd = min(end, startMap + rangeMap)
                # if it overlaps then "move" it based on the ranges
                if overlapEnd > overlapStart:
                    newValues.append((overlapStart - startMap + endMap, overlapEnd - startMap + endMap))
                    # append the remaining parts that doesn't overlap and wasn't shifted
                    if overlapStart > start:
                        seeds.append((start, overlapStart))
                    if overlapEnd < end:
                        seeds.append((overlapEnd, end))
                    break
            else:
                newValues.append((start, end))
        seeds = newValues
    print(min(seeds))
main()