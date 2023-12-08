with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip().splitlines()

resultPart1 = 0
counterIds = {}
for text in data:
    splittedText = text.split(':')
    cardId = int(splittedText[0].split()[1])
    numbers = splittedText[1].split('|')

    winningNumbers = numbers[0].strip().split()
    myNumbers = numbers[1].strip().split()

    counterPart1 = 0
    counterPart2 = 0

    # Part 1 and counter for part 2
    for number in myNumbers:
        if number in winningNumbers:
            counterPart1 = 1 if counterPart1 == 0 else counterPart1 * 2
            counterPart2 += 1

    # Part 2
    for x in range(0, counterPart2 + 1):
        nextId = cardId + x
        if nextId in counterIds:
            counterIds[nextId] += counterIds[cardId] if cardId != nextId else 1
        else:
            counterIds[nextId] = counterIds[cardId] if cardId != nextId else 1


    resultPart1 += counterPart1

print(f"Part 1: {resultPart1}") # 21558
print(f"Part 2: {sum(counterIds.values()}") # 10425665
