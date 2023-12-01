with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip().splitlines()
dataLength = len(data)

nums = [f"{n}" for n in range(1, 10)]

output = [0 for _ in range(len(data))]
for id in range(len(data)):
    firstNumber, lastNumber = False, False
    element = data[id]
    for index in range((len(element))):
        if firstNumber and lastNumber:
            break

        if  not firstNumber and element[index] in nums:
            output[id] += int(element[index]) * 10
            firstNumber = True

        lastId = len(element) - index - 1
        if not lastNumber and element[lastId] in nums:
            output[id] += int(element[lastId])
            lastNumber = True


print(sum(output))



