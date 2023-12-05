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
    for seed in tqdm(seeds):
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
resultPart2 = -1 
for seedId in range(0, len(seeds), 2):
    seedsPart2 = list(range(seeds[seedId], seeds[seedId] + seeds[seedId + 1]))
    result = obtainLowestLocation(seedsPart2, parsedData)
    resultPart2 = result if resultPart2 == -1 or result < resultPart2 else resultPart2


print(f"Part 1: {resultPart1}") # 825516882
print(f"Part 2: {resultPart2}") # 136096660