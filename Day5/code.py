from tqdm import tqdm # Using tqdm to add a progress bar

with open("input.txt", 'r') as f:
    data = f.read()

data = data.splitlines()

def parseData(data):
    parsedData = {}
    currentKey = ""
    for line in data:
        if line.strip() != "":
            if ":" in line:
                if "seeds" in line:
                    seeds = [int(x) for x in line.split(':')[1].strip().split()]

                else:
                    currentKey = line[:-1].replace(' map', '')
                    parsedData[currentKey] = []
                
            if currentKey != "" and currentKey not in line:
                parsedData[currentKey].append([int(x) for x in line.strip().split()])
    
    return seeds, parsedData


# Input data
seeds, parsedData = parseData(data)


# Part 1
def obtainLowestLocation(seeds, parsedData):
    result = -1
    for seed in tqdm(seeds, desc="Part 1"):
        seedDestination = 0
        value = seed
        for transformation in parsedData:
            for destination, source, length in parsedData[transformation]:
                if source <= value and value <= source + length - 1:
                    seedDestination = destination + value - source
                
            value = seedDestination if seedDestination != 0 else value
        
        if result == -1 or value < result:
            result = value
    
    return result


seeds, parsedData = parseData(data)

# Part 1
resultPart1 = obtainLowestLocation(seeds, parsedData)

# Part 2 - NOT TIME EFICIENT SOLUTION - 4 HOURS aprox
"""
resultPart2 = -1 
for seedId in range(0, len(seeds), 2):
    seedsPart2 = list(range(seeds[seedId], seeds[seedId] + seeds[seedId + 1]))
    result = obtainLowestLocation(seedsPart2, parsedData)
    resultPart2 = result if resultPart2 == -1 or result < resultPart2 else resultPart2
"""

# Part 2 - REVERSE LOOKUP (from location to seed) - 53 min.
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

humidityToLocation, humiditySources = sortRange(parsedData['humidity-to-location'])
seedsRanges = getSeedRanges(seeds)


resultPart2 = 0 # 136.096.660
for locationId in range(len(humidityToLocation)):
    lowLocation, highLocation =  humidityToLocation[locationId][0], humidityToLocation[locationId][1]
    sourceLowLoc, sourceHighLoc = humiditySources[locationId][0], humiditySources[locationId][1]

    n = 0 if locationId == 0 else lowLocation
    for number in tqdm(range(n, highLocation), desc="Part 2"):
        currentDestination = number
        allPossible = [currentDestination]
        for transformation in list(reversed(parsedData.keys()))[:]:
            localData = parsedData[transformation]
            for destination, source, length in localData:
                lowestDestination, highestDestination = destination, destination + length - 1
                lowestSource = source
                if lowestDestination <= currentDestination and highestDestination >= currentDestination:
                    currentDestination = lowestSource + (currentDestination - lowestDestination)
                    break
            
            allPossible.append(currentDestination)
        
        seed = allPossible[-1]
        location = number
        
        for low, high in seedsRanges:
            if low <= seed  and high >= seed:
                resultPart2 = location
                break

        # There is probably a cleaner way to do this
        else:
            continue
        break
    
    else:
        continue
    
    break


print(f"Part 1: {resultPart1}") # 825516882
print(f"Part 2: {resultPart2}") # 136096660