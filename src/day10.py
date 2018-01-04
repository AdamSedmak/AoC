def xorList(inputList):
	result = 0
	for elem in inputList:
		result = result ^ elem
	#print("Neki rezultat:" + str(hex(result)))
	return hex(result)

with open("day10.txt") as f:
    line = f.readline()

lengths = [ord(c) for c in line]
addedLengths = [17, 31, 73, 47, 23]
lengths.extend(addedLengths)
print(lengths)

initList = list(range(256))
skip = 0
currentPos = 0

for length in lengths:
	length = int(length)
	newList = []
	i = 0
	while length:
		if (currentPos + i) / len(initList):
			offset = (currentPos + i) % len(initList)
		else:
			offset = currentPos + i
		newList.append(initList[offset])
		length -= 1
		i += 1
	newList.reverse()
	for j, element in enumerate(newList):
		if (currentPos + j) / len(initList):
			offset = (currentPos + j) % len(initList)
		else:
			offset = currentPos + j
		initList[offset] = element
	currentPos += i + skip
	skip += 1

value = initList[0] * initList[1]
print('Multiplying first two numbers gives: ' + str(value))

print("------------------------------------------------------")

initList = list(range(256))
skip = 0
currentPos = 0
n = 64
resultList = []

while n:
	for length in lengths:
		length = int(length)
		newList = []
		i = 0
		while length:
			if (currentPos + i) / len(initList):
				offset = (currentPos + i) % len(initList)
			else:
				offset = currentPos + i
			newList.append(initList[offset])
			length -= 1
			i += 1
		newList.reverse()
		for j, element in enumerate(newList):
			if (currentPos + j) / len(initList):
				offset = (currentPos + j) % len(initList)
			else:
				offset = currentPos + j
			initList[offset] = element
		currentPos += i + skip
		skip += 1
	n -= 1
print(initList)

initPos = 0
n = 16

while n:
	resultList.append(xorList(initList[initPos:initPos+16]))
	initPos += 16
	n -= 1

print(resultList)






