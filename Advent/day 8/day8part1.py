def main():
    file = open("/Users/dyee25/Desktop/Advent/day 8/day8.txt").read().splitlines()

    steps = file[0]
    elements = file[2:-1]
    finalElements = {}
    for i in range(len(elements)):
        key, value = elements[i].split(" = ")
        finalElements[key] = value
    print(finalElements["AAA"][1:4])
    values = "AAA"
    ans = 0
    i = 0
    while values != "ZZZ":
        if i >= len(steps):
            i = 0
        if steps[i] == "R": 
            values = finalElements[values][6:9]
            print(values)
        else:
            values = finalElements[values][1:4]
            print(values)
        ans += 1
        i += 1
    print(ans)
            
        
main()