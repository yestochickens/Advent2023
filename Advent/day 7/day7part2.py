def findDuplicates(hand):
    count = {}
    for letter in hand:
        if letter in count:
            count.update({letter: count.get(letter) + 1})
        else:
            count[letter] = 1
    countSorted = dict(sorted(count.items(), key = lambda item: item[1], reverse = True))
    if "J" in countSorted:
        # finds the first key of count
        keysList = list(countSorted.keys())
        firstKey = keysList[0]
        if firstKey == "J":
            if countSorted.get("J") == 5:
                # if all Jokers count will remain 5 so it returns 5 of a kind
                countSorted["J"] = countSorted["J"]
            else:
                # adds # of Jokers to second highest number of duplicates if Jokers is the most duplicates
                countSorted[keysList[1]] += countSorted["J"]
                countSorted["J"] = 0
        else:
            # adds # of Jokers to highest number of duplicates
            countSorted[firstKey] += countSorted["J"]
            countSorted["J"] = 0
    sortedValues = []
    for item in countSorted.values():
        sortedValues.append(item)
    sortedValues.sort(reverse = True)
    # five of a kind
    if max(countSorted.values()) == 5:
        return 6
    # four of a kind
    if max(countSorted.values()) == 4:
        return 5
    if max(countSorted.values()) == 3:
        # full house
        if sortedValues[1] == 2:
            return 4
        # 3 of a kind
        else:
            return 3
    if max(countSorted.values()) == 2:
        # 2 pair
        if sortedValues[1] == 2:
            return 2
        # 1 pair
        else:
            return 1
    # no pair
    if max(countSorted.values()) == 1:
        return 0
    
        
# when the list is sorted A is best followed by K, Q, J, T, 9, 8.... etc
letterMap = {"T": "A", "J": "0", "Q": "C", "K": "D", "A": "E"}
hands = []
for line in open("/Users/dyee25/Desktop/Advent/day 7/day7.txt"):
    hand, bid = line.split(" ")
    # adds 0-7 based on how many duplicates to front of hand because that is the most important factor when sorting
    hand = str(findDuplicates(hand)) + hand
    # replaces "facecards" with new letters from letterMap so it is sorted correctly
    replacedHand = [letterMap.get(letter, letter) for letter in hand]
    hand = " ".join(replacedHand)
    hands.append((hand, bid))
ans = 0
hands.sort()
for i in range(len(hands)):
    ans += int(hands[i][1]) * (i+1)
print(ans)
