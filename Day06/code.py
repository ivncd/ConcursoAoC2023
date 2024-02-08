with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip().splitlines()

times = data[0].strip().split(':')[1].split()
distances = data[1].strip().split(':')[1].split()

times2 = [int(''.join(times))]
distances2 = [int(''.join(distances))]

def getResult(times, distances):
    result = 1
    for id in range(len(times)):
        time, distance = int(times[id]), int(distances[id])
        counter = 0

        for ms in range(1, time):
            if ms*(time - ms) > distance:
                counter += 1
        
        result *= counter
    
    return result

resultPart1 = getResult(times, distances)
resultPart2 = getResult(times2, distances2)


print(f"Part1: {resultPart1}") # 131376
print(f"Part2: {resultPart2}") # 34123437




