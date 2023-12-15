with open('input.txt') as f:
    data = f.read()

data = data.split(',')


def getHASHNumber(text : str) -> int:
    result = 0
    for letter in text:
        result += ord(letter)
        result *= 17
        result %= 256

    return result

resultPart1 = 0
lensBox, lensValue = {}, {}
for string in data:
    if '-' in string:
        label = string[:-1]
        hashNumber = getHASHNumber(label) 

        if hashNumber in lensBox:
            if label in lensBox[hashNumber]:
                lensBox[hashNumber].remove(label)

    elif '=' in string:
        label, value = string.split('=')
        hashNumber = getHASHNumber(label) 
        if hashNumber in lensBox:
            if label not in lensBox[hashNumber]:
                lensBox[hashNumber].append(label)
                lensValue[label] = int(value)
            
            else:
                lensValue[label] = int(value)
        
        else:
            lensBox[hashNumber] = [label]
            lensValue[label] = int(value)


    # Part 1
    resultPart1 += getHASHNumber(string)


resultPart2 = 0
for box in lensBox:
    for id, label in enumerate(lensBox[box]):
        result = (1 + box) * (id + 1) * lensValue[label]
        resultPart2 += result



print('Part 1:', resultPart1)
print('Part 2:', resultPart2)