with open('day5.txt') as f:
    lines = f.readlines()   #whole file stored as list

lines = [x.strip() for x in lines]
lines = map(int, lines)

curr = 0
cnt = 0
while curr < len(lines):
    prev = curr
    curr += lines[curr]
    lines[prev] += 1
    cnt += 1
print('Number of steps is: ' + str(cnt))
print('--------------------------------------')

with open('day5.txt') as f:
    lines = f.readlines()   #whole file stored as list

lines = [x.strip() for x in lines]
lines = map(int, lines)

print(lines)

curr = 0
cnt = 0
while curr < len(lines):
    prev = curr
    curr += lines[curr]
    if lines[prev] < 3:
        lines[prev] += 1
    else:
        lines[prev] -= 1
    cnt += 1
print('Number of steps is: ' + str(cnt))