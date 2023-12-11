with open('input.txt', 'r') as f:
    data = f.read()

data = [list(row) for row in data.strip().splitlines()]

def getTextData(data):
    rowVoidLocation, columnVoidLocation = [], []
    galaxyDict, galaxyCounter =  {}, 1
    for y, row in enumerate(data):
        if '#' not in row:
            rowVoidLocation.append(y)
        
        else:
            for x, letter in enumerate(row):
                if letter == '#':
                    data[y][x] = f"{galaxyCounter}"
                    galaxyDict[f"{galaxyCounter}"] = (x, y)
                    galaxyCounter += 1

    for x in range(len(data[0])):
        if all([data[y][x] == '.' for y in range(len(data))]):
            columnVoidLocation.append(x)

    return galaxyDict, rowVoidLocation, columnVoidLocation



def getAllDistances(galaxyDict, rowVoidLocation, columnVoidLocation, multiplier):
    galaxyKeys, allDistances = list(galaxyDict.keys()), 0
    for galaxyId, fromGalaxy in enumerate(galaxyKeys):
        originX, originY = galaxyDict[fromGalaxy]
        for destinationGalaxy in galaxyKeys[galaxyId + 1:]:
            destinationX, destinationY = galaxyDict[destinationGalaxy]
            
            addX = len([x for x in columnVoidLocation if ((originX < x and x < destinationX) or (destinationX < x and x < originX))])
            distanceX = ((destinationX - originX) * (-1 if (destinationX - originX) < 0 else 1)) + (multiplier - 1) * addX
            
            addY = len([y for y in rowVoidLocation if ((originY < y and y < destinationY) or (destinationY < y and y < originY))])
            distanceY = ((destinationY - originY) * (-1 if (destinationY - originY) < 0 else 1)) + (multiplier - 1) * addY 

            allDistances += distanceX + distanceY 
    
    return allDistances


galaxyDict, rowVoidLocation, columnVoidLocation = getTextData(data)

resultPart1 = getAllDistances(galaxyDict, rowVoidLocation, columnVoidLocation, 2)
print(f"Part 1: {resultPart1}") # 10289334


resultPart2 = getAllDistances(galaxyDict, rowVoidLocation, columnVoidLocation, 1000000)
print(f"Part 2: {resultPart2}") # 649862989626


