def checkEqual(listOfChildren):
   return len(set(listOfChildren)) <= 1

with open('day7.txt') as f:
    lines = f.readlines()   #whole file stored as list
lines = [x.strip() for x in lines]

listOfBottoms = []
listOfPrograms = []

for program in lines:
	name = program.split(' ')
	if len(name) > 2:
		i = 3
		while i < len(name):
			listOfPrograms.append(name[i].strip(','))
			i += 1
	listOfBottoms.append(name[0])

for bottom in listOfBottoms:
	if bottom not in listOfPrograms:
		print('Most bottom program is: ' + bottom)
		break

programWeightPairs = {}
truePairs = {}


for program in lines:
	name = program.split(' ', 3)
	programWeightPairs[name[0]] = int(name[1].strip(')').strip('('))


for program in lines:
	childList = []
	name = program.split(' ', 3)			#name[0] is parent process
	currSum = int(name[1].strip(')').strip('('))
	if len(name) > 2:
		children = name[3].split(', ')		#all child processes
		for child in children:
			childList.append(programWeightPairs[child])
		if checkEqual(childList):
			currSum += sum(childList)
		truePairs[name[0]] = currSum
print(truePairs)






	
