def main():
    file = open("/Users/dyee25/Desktop/Advent/day 5/day5.txt", "r")
    table = []
    # makes the seed array
    for line in file:
        newLine = line.split("\n")
        newNewLine = newLine[0].split(" ")
        table.append(newNewLine)
    # makes the strings into ints
    seed = [int(i) for i in (table[0][1:])]
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
    #print(intMapValues)

    for l in range(7): 
        seed = (map(seed,intMapValues[l]))
    print(seed)
    # finds smallest number
    smallestNumber = 99999999999999999
    for i in range(len(seed)): 
        if seed[i] < smallestNumber:
            smallestNumber = seed[i]
    print(smallestNumber)

def map(input, map):
    for s in range(len(input)):
        for i in range(len(map)):
            if (map[i][1]) <= input[s] <= (map[i][1] + (map[i][2] - 1)):
                input[s] = map[i][0] + (input[s] - map[i][1])
                break
    return(input)

main()