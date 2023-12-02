with open('input.txt', 'r') as f:
    data = f.read()
data = data.strip().splitlines()

# Parte 1
output = []
for text in data[:]:
    firstNumber, lastNumber = 0, 0
    for letterId in range(len(text)):
        if firstNumber != 0 and lastNumber != 0:
            break

        if text[letterId].isdigit() and firstNumber == 0:
            firstNumber = int(text[letterId]) * 10
        
        lastLetterId = len(text) - letterId - 1
        if text[lastLetterId].isdigit() and lastNumber == 0:
            lastNumber = int(text[lastLetterId])

    output.append(firstNumber + lastNumber)



# Parte 2
numsInLetter = {"one" : "1", "two" : "2", "three" : "3",
                "four" : "4", "five" : "5", "six" : "6",
                "seven" : "7", "eight" : "8", "nine" : "9"}


output2 = []
for text in data:
    firstNumber, lastNumber = 0, 0
    for letterId in range(len(text)):
        if firstNumber != 0 and lastNumber != 0:
            break

        if firstNumber == 0:
            if text[letterId].isdigit():
                firstNumber = int(text[letterId])
            
            for num in numsInLetter:
                if num in text[:letterId]:
                    firstNumber = int(numsInLetter[num])
        
        lastLID = len(text) - letterId - 1
        if lastNumber == 0:
            if text[lastLID].isdigit():
                lastNumber = int(text[lastLID])
            
            for num in numsInLetter:
                if num in text[lastLID:]:
                    lastNumber = int(numsInLetter[num])
        
    output2.append(firstNumber*10 + lastNumber)


print(f"Parte 1: {sum(output)}")
print(f"Parte 2: {sum(output2)}")
