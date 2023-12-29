def allZ(array):
    for letter in array:
        if letter[-1] == 'Z':
            continue
        else:
            return False
    return True

def main():
    file = open("/Users/dyee25/Desktop/Advent/day 8/day8.txt").read().splitlines()

    steps = file[0]
    elements = file[2:]
    finalElements = {}
    for i in range(len(elements)):
        key, value = elements[i].split(" = ")
        finalElements[key] = value
    values = []
    for key in finalElements.keys():
        if key[-1] == "A":
            values.append(key)
    ans = 0
    index = 0
    while not allZ(values):
        for i in range(len(values)):
            if index >= len(steps):
                index = 0
            if steps[index] == "R": 
                values[i] = finalElements[values[i]][6:9]
            else:
                values[i] = finalElements[values[i]][1:4]
            ans += 1
        index += 1
        if ans % 1000 == 0:
            print(ans)

    print(ans)
            
        
main()