# https://projecteuler.net/problem=9

def getProduct(values):
    prod = 1
    for value in values:
        prod = value*prod
    return prod

file = open("input.txt", "r")

lastValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
highProd = 1
for line in file:
    line.rstrip()
    for number in line:
        if number == "\n": continue
        lastValues.pop(0)
        lastValues.append(int(number))
        currentProd = getProduct(lastValues)
        if currentProd > highProd:
            highProd = currentProd


print(highProd)