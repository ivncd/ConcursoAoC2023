"""

It isn't working I used the bruteforce method that took 4 hours,
When testing, it works but when using the input it gives me

Part2: 55716176 

whereas it shouldn't be like that.

It was interesting but tedious
"""


from tqdm import tqdm


with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip().splitlines()

def parseData(data):
    parsedData = {}
    currentKey = ""
    seeds = [int(x) for x in data[0].split(':')[1].strip().split()]
    for line in data[1:]:
        if line.strip() != "":
            if ":" in line:
                    currentKey = line[:-1].replace(' map', '')
                    parsedData[currentKey] = []
                
            elif currentKey != "" and currentKey not in line:
                parsedData[currentKey].append([int(x) for x in line.strip().split()])
    
    return seeds, parsedData


def sortRange(data):
    """
    Funcition to sort ranges from low to high
    """
    orderedResult = [[data[0][0], data[0][0] + data[0][2] - 1]]
    orderedSourcesResult = [[data[0][1], data[0][1] + data[0][2] - 1]]
    for id in range(1, len(data)):
        destination, source, length = data[id][0], data[id][1], data[id][2]
        lowestDestinationRange = [destination, destination + length - 1]
        lowestSource = [source, source + length - 1]
        for resultId in range(len(orderedResult)):
            if lowestDestinationRange[0] < orderedResult[resultId][0]:
                orderedResult.insert(resultId, lowestDestinationRange)
                orderedSourcesResult.insert(resultId, lowestSource)
                break
            
            elif resultId == len(orderedResult) - 1:
                orderedResult.append(lowestDestinationRange)
                orderedSourcesResult.append(lowestSource)

    return orderedResult, orderedSourcesResult


def getSeedRanges(seeds):
    seedsRange = []
    for seedId in range(0, len(seeds), 2):
         seedsRange.append([seeds[seedId], seeds[seedId] + seeds[seedId + 1] - 1])

    return seedsRange

seeds, parsedData = parseData(data)
humidityToLocation, humiditySources = sortRange(parsedData['humidity-to-location'])
seedsRanges = getSeedRanges(seeds)


resultPart2 = 0 # 136.096.660
for locationId in range(len(humidityToLocation)):
    lowLocation, highLocation =  humidityToLocation[locationId][0], humidityToLocation[locationId][1]
    sourceLowLoc, sourceHighLoc = humiditySources[locationId][0], humiditySources[locationId][1]

    for number in tqdm(range(1, sourceHighLoc)):
        currentDestination = number
        allPossible = [currentDestination]
        for transformation in list(reversed(parsedData.keys()))[1:]:
            localData = parsedData[transformation]
            for destination, source, length in localData:
                lowestDestination, highestDestination = destination, destination + length - 1
                lowestSource = source
                if lowestDestination <= currentDestination and highestDestination >= currentDestination:
                    currentDestination = lowestSource + (currentDestination - lowestDestination)
                    break
            
            #print(destination, source, length, transformation, currentDestination)
            allPossible.append(currentDestination)


        seed = allPossible[-1]
        location = lowLocation + (number - sourceLowLoc) if number >= sourceLowLoc else number
        
        
        for low, high in seedsRanges:
            if low <= seed  and high >= seed:
                resultPart2 = location
                break

        else:
            continue
        break
    
    else:
        continue
    
    break


print(f"Part2: {resultPart2}") # Wrong answer it works for tests but not for input -> 55716176
