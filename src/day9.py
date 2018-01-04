curSum = 0
garbage = False
escaped = False
value = 0
garbageCnt = 0

with open('day9.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            print("End of file")
            break
        #print(c)
        if escaped:
            escaped = False
            continue
        elif c == "!":
            escaped = True
            continue
        if c == "<":
            garbage = True
        elif c == ">":
            garbageCnt -= 1
            garbage = False
        if garbage:
            garbageCnt += 1
            continue
        if c == "{":
            value += 1
        if c == "}":
            curSum += value
            value -= 1

print("There are " + str(garbageCnt) + " non-canceled characters!")
print("Total score for all groups is: " + str(curSum))
