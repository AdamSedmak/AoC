with open("day11.txt") as f:
	line = f.readline()
line = line.strip().split(',')
#print(line)

nCnt = 0
neCnt = 0
seCnt = 0
sCnt = 0
swCnt = 0
nwCnt = 0

for elem in line:
	if elem == 'n':
		nCnt += 1
	elif elem == 'ne':
		neCnt += 1
	elif elem == 'se':
		seCnt += 1
	elif elem == 's':
		sCnt += 1
	elif elem == 'sw':
		swCnt += 1
	else:
		nwCnt += 1

print("N: " + str(nCnt) + "; NE: " + str(neCnt) + "; SE: " + str(seCnt) + "; S: " + str(sCnt) + "; SW: " + str(swCnt) + "; NW: " + str(nwCnt))

nVSs = nCnt - sCnt
neVSsw = neCnt - swCnt
nwVSse = nwCnt - seCnt

print("upORdown: " + str(nVSs) + "; uprightORdownleft: " + str(neVSsw) + "; upleftORdownright: " + str(nwVSse))

movLst = [nVSs, neVSsw, nwVSse]
print(movLst)

totalDifference = movLst[0] + movLst[1] + movLst[2] - min(movLst)

print("Total number of steps is:" + str(totalDifference)) 

