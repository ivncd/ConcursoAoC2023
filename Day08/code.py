from math import lcm

with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip().splitlines()

instructions = data[0]
network = data[2:]
map = {line.split(' = ')[0] : line.split(' = ')[1][1:-1].split(', ') for line in network}

# Part 1
currentPosition, counter = 'AAA', 0
while currentPosition != 'ZZZ':
    for instruction in instructions:
        if currentPosition == 'ZZZ':
            break

        currentPosition = map[currentPosition][1] if instruction == 'R' else map[currentPosition][0] # R L
        counter += 1

#Part 2
counter2 = 0
startingPositions = [key for key in map if key[-1] == 'A']
zPositions = [{} for _ in range(len(startingPositions))]
multipliers = [0 for _ in range(len(startingPositions))]
for positionId, position in enumerate(startingPositions):
    foundPosition, counter2 = False, 1
    while not foundPosition:
        for instruction in instructions:
            currentPosition = map[startingPositions[positionId]][1] if instruction == 'R' else map[startingPositions[positionId]][0] # R L
            if currentPosition[-1] == 'Z':
                multipliers[positionId] = counter2
                foundPosition = True
                break
                
                # -- Edit after reviewing the code -- #
                #if currentPosition not in zPositions[positionId]: # Unncessary because there is only one unique XXZ for each XXA
                    #zPositions[positionId][currentPosition] = counter2 # Unnecessary, explained below
            
                    # Given that distance from XXA to XXZ is always equal to the distance from XXZ to XXZ (cyclic), then we can just 
                    # do the LCM of the distance and get the lowest point they meet

                #else:
                    #multipliers[positionId] = (counter2) - zPositions[positionId][currentPosition]
                    #Unnecessary because: counter2 - zPositions[positionId][currentPosition] == zPositions[positionId][currentPosition]
                
                # ---------------------------------- #

            startingPositions[positionId] = currentPosition
            counter2 += 1


print('Part 1: ', counter) # 20093
print('Part 2: ', lcm(*multipliers)) # 22103062509257