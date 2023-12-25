with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip().splitlines()

def getCrossedLocation(path1 : list[list[int], list[int]], path2 : list[list[int], list[int]]) -> [int, int, int, int]:
    x1, y1, _ = path1[0]
    vx1, vy1, _ =  path1[1]

    x2, y2, _ = path2[0]
    vx2, vy2, _ =  path2[1]

    t2 = ((x2-x1)*vy1 - (y2 - y1)*vx1)/(vx1*vy2 - vy1*vx2)
    t1 = (y2 + vy2*t2 - y1)/vy1
            
    x = x1 + vx1*t1
    y = y1 + vy1*t1

    return x, y, t1, t2


paths = [[[int(x1.strip()) for x1 in x.split(',')] for x in line.split('@')] for line in data]

resultPart1 = 0
lowestPosition, highestPosition = 200000000000000, 400000000000000
for id1 in range(len(paths) - 1):
    path1 = paths[id1]
    vx1, vy1 = path1[1][0], path1[1][1]
    for id2 in range(id1 + 1, len(paths)):
        path2 = paths[id2]
        vx2, vy2 = path2[1][0], path2[1][1]

        if (vx1*vy2 - vy1*vx2) != 0: # Not parallel
            x, y, t1, t2 = getCrossedLocation(path1, path2)
            if lowestPosition <= x <= highestPosition and lowestPosition <= y <= highestPosition and t1 >= 0 and t2 >= 0:
                resultPart1 += 1

                
                
print('Part 1:', resultPart1) # 13149