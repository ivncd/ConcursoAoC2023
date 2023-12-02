RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

with open("input.txt", "r") as f:
    data = f.read().strip().splitlines()


resultPart1 = 0
resultPart2 = 0
for text in data:
    splitText = text.split(':')
    gameId, cubesList = int(splitText[0].split(' ')[-1]), splitText[1].replace(',', ';').split(';')  

    isImpossible = False # Part 1
    cubeCounter = {"green": 0, "blue": 0, "red": 0} # Part 2
    for cube in cubesList:
        cubeNumber = int(cube.strip().split(' ')[0])
        cubeColor = cube.strip().split(' ')[1]

        # Part 1
        if (cubeColor == "blue" and cubeNumber > BLUE_CUBES) or (cubeColor == "green" and cubeNumber > GREEN_CUBES) or cubeColor == "red" and (cubeNumber > RED_CUBES):
            isImpossible = True
    
        # Part 2
        if (cubeNumber > cubeCounter[cubeColor]):
            cubeCounter[cubeColor] = cubeNumber

    
    if not isImpossible:
        resultPart1 += gameId

    resultPart2 += cubeCounter['blue'] * cubeCounter['green'] * cubeCounter['red'] 

        
print(f"Part 1: {resultPart1}")
print(f"Part 2: {resultPart2}")