with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip().splitlines()

def getSolution(rows, part2 = False):
    valueInHistory = 0
    for rowId in range(0, len(rows)):
        valueInHistory = rows[-(rowId + 1)][-1] + valueInHistory if not part2 else rows[-(rowId + 1)][0] - valueInHistory
    
    return valueInHistory


resultPart1, resultPart2 = 0, 0
for line in data:
    rows = [[int(x) for x in line.split()]]
    lastRow = rows[0]
    while not all([x == 0 for x in lastRow]):
        newRow = []
        for numberId in range(len(lastRow[:-1])):
            newNumber = lastRow[numberId + 1] - lastRow[numberId]
            newRow.append(newNumber)

        lastRow = newRow
        rows.append(newRow)

    resultPart1 += getSolution(rows)
    resultPart2 += getSolution(rows, part2=True)


print(f"Part 1: {resultPart1}")
print(f"Part 2: {resultPart2}")

    