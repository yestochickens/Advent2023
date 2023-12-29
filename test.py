def allZ(array):
    return all(letter[-1] == 'Z' for letter in array)

def main():
    file_path = "/Users/dyee25/Desktop/Advent/day 8/day8.txt"
    with open(file_path) as file:
        lines = file.read().splitlines()

    steps = lines[0]
    elements = lines[2:]
    
    finalElements = {key: value for key, value in (e.split(" = ") for e in elements)}
    
    values = {key for key in finalElements if key[-1] == "A"}
    
    ans = 0
    index = 0
    while True:
        for key in values:
            if index >= len(steps):
                index = 0
            value = finalElements[key]
            values.remove(key)
            if steps[index] == "R":
                values.add(value[6:9])
            else:
                values.add(value[1:4])
            ans += 1
        index += 1
        if allZ(values):
            break
        if ans % 1000 == 0:
            print(ans)

    print(ans)

if __name__ == "__main__":
    main()
