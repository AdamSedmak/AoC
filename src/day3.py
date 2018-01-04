import math

inputNumber = 361527

minBiggerSquare = math.ceil(math.sqrt(inputNumber))
if minBiggerSquare % 2 == 0:
    minBiggerSquare += 1

print(minBiggerSquare)
squareNumber = math.ceil(minBiggerSquare / 2)
print(squareNumber)

maxSmallerSquare = minBiggerSquare - 2
difference = inputNumber - math.pow(maxSmallerSquare, 2)
print("Difference: " + str(difference))

upwards = minBiggerSquare - 1 - difference      #how much will we go up from bottom right
print("Upwards we go: " + str(upwards) + " points!")
additionalUpwardsDirection = squareNumber - 1 - upwards
print(additionalUpwardsDirection)

manhattanDistance = additionalUpwardsDirection + squareNumber - 1

print("Manhattan distance is: " + str(manhattanDistance))