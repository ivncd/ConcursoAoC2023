pruebas = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip().splitlines()

diggedTerrain = []
currentPosition = (0,0)


for line in data:
    letter, times, color = line.split()[0], int(line.split()[1]), line.split()[2][1:-1]
    if letter == 'U': # UP
        add = (0, -1)
    elif letter == 'D': # DOWN
        add = (0, 1)
    elif letter == 'L':
        add = (-1, 0)
    elif letter == 'R':
        add = (1, 0)
    
    #print(line)
    for more in range(times):
        x, y = currentPosition
        height = len(diggedTerrain)

        if y < 0:
            diggedTerrain.insert(0, [])
            y = 0

        elif height <= y:
            diggedTerrain.append([])

        
        width = len(diggedTerrain[y])

        if x < 0:
            for line in diggedTerrain:
                line.insert(0, '.')
            
            x = 0

        if width <= x:
            difference = x - width
            for mx in range(difference):
                diggedTerrain[y].append('.')
            
            diggedTerrain[y].append('#')
        else:
            diggedTerrain[y][x] = '#'
        
        currentPosition = (x + add[0], y + add[1])


# Adjust 
maxwidth = 0
for line in diggedTerrain:
    if len(line) > maxwidth:
        maxwidth =  len(line)

for y, line in enumerate(diggedTerrain):
    difference = maxwidth - len(line)
    diggedTerrain[y] += ['.' for _ in range(difference)]



total = ""
for line in diggedTerrain:
    total += ''.join(line) + '\n'

with open('out.txt', 'w+') as f:
    f.write(total) # LOW

