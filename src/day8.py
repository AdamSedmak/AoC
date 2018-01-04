with open('day8.txt') as f:
    lines = f.readlines()   #whole file stored as list
lines = [x.strip() for x in lines]

regValue = {}

for line in lines:
	splitted = line.split(' ');
	if splitted[0] not in regValue:
		regValue[splitted[0]] = 0

print(regValue)

biggest = 0

for line in lines:
	splitted = line.split(' ');
	register = splitted[0]
	command = splitted[1]
	value = int(splitted[2])
	condReg = splitted[4]
	condition = splitted[5]
	condValue = splitted[6]

	if eval("regValue[condReg] " + condition + condValue): #check if cond is true
		if command == 'inc':
			regValue[register] += value
			if regValue[register] >= biggest:
				biggest = regValue[register]
		else:
			regValue[register] -= value
			if regValue[register] >= biggest:
				biggest = regValue[register]

print(max(zip(regValue.values(), regValue.keys())))
print('Maximum value ever held was: ' + str(biggest))
