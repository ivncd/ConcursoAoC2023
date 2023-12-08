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
    secondPosition = False
    while not secondPosition:
        for instruction in instructions:
            currentPosition = map[startingPositions[positionId]][1] if instruction == 'R' else map[startingPositions[positionId]][0] # R L
            if currentPosition[-1] == 'Z':
                if currentPosition not in zPositions[positionId]:
                    zPositions[positionId][currentPosition] = counter2 + 1
                    
                else:
                    multipliers[positionId] =  (counter2 + 1) - zPositions[positionId][currentPosition]
                    secondPosition = True
                    break
            
            startingPositions[positionId] = currentPosition
            counter2 += 1


print('Part 1: ', counter)
print('Part 2: ', lcm(*multipliers))

