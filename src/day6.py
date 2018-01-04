with open('day6.txt') as f:
    initial = f.readlines()   #whole file stored as list
initial = [x.strip() for x in initial]
initial = map(int, initial)

listOfLists = []
listOfLists.append(initial)
lastAdded = list(initial)

cnt = 0
loopBeginning = 0
while True:
    index = 0
    biggest = lastAdded[index]
    for i, value in enumerate(lastAdded):
        if value > biggest:
            biggest = value
            index = i
    lastAdded[index] = 0
    while biggest > 0:
        index += 1
        if index / len(lastAdded) > 0:
            index = index % len(lastAdded)
        lastAdded[index] += 1
        biggest -= 1
    cnt += 1
    if lastAdded in listOfLists:
        for i, l in enumerate(listOfLists):
            if lastAdded == l:
                loopBeginning = i
                break
        break
    newList = list(lastAdded)
    listOfLists.append(newList)
#print(listOfLists)
print('Number of redistributions is: ' + str(cnt))
print('Number of cycles is: ' + str(cnt - loopBeginning))


