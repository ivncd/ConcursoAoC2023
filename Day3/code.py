def isSymbol(text):
    for letter in text:
        if not letter.isdigit() and letter != '.':
            return True, letter == '*'

    return False, False

def checkNear(lineId, letterId, numberlen, data):
    minusOne = 1 
    validNumber, isGear = False, False
    gearId, gearLine = "", lineId

    # Check left
    if not validNumber:
        possibleText = data[lineId][letterId - numberlen - 1]
        validNumber, isGear = isSymbol(possibleText)
        if isGear:
            gId = letterId - numberlen - 1


    # Check right
    if letterId < len(data[lineId]) and not validNumber:
        possibleText = data[lineId][letterId]
        validNumber, isGear = isSymbol(possibleText)
        if isGear:
            gId = letterId

    # Check up
    if lineId > 0 and not validNumber:
        lastLine = data[lineId - 1]
        possibleText = lastLine[letterId - numberlen - 1: letterId + 1]
        validNumber, isGear = isSymbol(possibleText)
        if isGear:
            gId = (letterId - numberlen - 1) + possibleText.find('*')
            gearLine = lineId - 1

    # Check down
    if lineId < len(data) - 1 and not validNumber:
        nextLine = data[lineId + 1]
        possibleText = nextLine[letterId - numberlen - 1: letterId + 1]
        validNumber, isGear = isSymbol(possibleText)
        if isGear:
            gId = (letterId - numberlen - 1) + possibleText.find('*')
            gearLine = lineId + 1

    if isGear and validNumber:
        gearId = f"{gearLine}{gId}"

    return validNumber, gearId


with open('input.txt', 'r') as f:
    data = f.read()

data = ['.' + d.strip() + '.' for d in data.splitlines()] # Adding '.' at both sides 
gears = {}

outputPart1 = []
for lineId, line in enumerate(data):
    numberlen = 0
    for id, letter in enumerate(line):
        if letter.isdigit():
            numberlen += 1 
        
        else:
            if numberlen > 0:
                number = int(line[id - numberlen: id])
                validNumber, gearId = checkNear(lineId, id, numberlen, data) #n pruebas
                if validNumber:
                    outputPart1.append(number)

                    # Part 2 - Adding gear location and numbers near
                    if gearId != "":
                        if gearId in gears:
                            gears[gearId].append(number)
                        
                        else:
                            gears[gearId] = [number]
                
                numberlen = 0


outputPart2 = []
for gear in gears:
    numbers = gears[gear]
    if len(numbers) == 2:
        outputPart2.append(numbers[0] * numbers[1])

print(f"Part 1: {sum(outputPart1)}") #537832
print(f"Part 2: {sum(outputPart2)}") #81939900

