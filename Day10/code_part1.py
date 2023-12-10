with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip().splitlines()

rows = ['.' + x.strip() + '.' for x in data]
rows.insert(0, '.' * len(rows[0]))
rows.append('.' * len(rows[0]))

positionFromX = {'-' : (1, 0),  'L': (0, -1), 'J': (0, -1), '7': (0, 1), 'F': (0, 1)}
positionFromY = {'|' : (0 , 1), 'L': (1, 0), 'J': (-1, 0), '7': (-1, 0), 'F': (1,0)}

EAST, WEST = ['J', '-', '7'], ['L', '-', 'F']
NORTH, SOUTH = ['|', 'F', '7'], ['|', 'J', 'L']


startingPosition = [0, 0]
for rowId in range(len(rows)):
    if 'S' in rows[rowId]:
        startingPosition = [rows[rowId].index('S'), rowId]
        break

def getStartingPosition(x, y, rows):
    total = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    followingPosition = None
    for ax, ay in total:
        letter = rows[y + ay][x + ax]
        if letter != '.':
            if ax != 0:
                if (ax == 1 and letter in EAST) or (ax == -1 and letter in WEST):
                    followingPosition = (x + ax, y + ay)
                    break

            else:
                if (ay == 1 and letter in NORTH) or (ay == -1 and letter in SOUTH):
                    followingPosition = (x + ax, y + ay)
                    break
    
    return followingPosition


counter, isBack = 1, False
x, y = startingPosition
fX, fY = getStartingPosition(x, y, rows)
while not isBack:
    letter = rows[fY][fX]
    if letter == 'S' and counter > 1:
        break

    letterAdd = positionFromY[letter] if fY != y else positionFromX[letter]

    if (fX < x and letter == '-') or (fY < y and letter == '|') :
        letterAdd = [x*-1  for x in letterAdd]
    
    x, y = fX, fY
    fX, fY = fX + letterAdd[0], fY + letterAdd[1]

    counter += 1


print(f"Part 1: {counter//2}")










