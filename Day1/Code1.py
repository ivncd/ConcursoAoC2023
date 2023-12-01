with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip().splitlines()

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbersWords = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

partOne, partTwo = [], []
for text in data:
    firstIndex, lastIndex = len(text) - 1, len(text) - 1
    for number in numbers:
        if number in text:
            firstPosition = text.find(number)
            if firstPosition < firstIndex:
                firstIndex = firstPosition
            
            lastPosition = text[::-1].find(number)
            if lastPosition < lastIndex:
                lastIndex = lastPosition
    
    firstNumber, lastNumber = int(text[firstIndex]), int(text[::-1][lastIndex])
    partOne.append(firstNumber * 10 + lastNumber)

    # Part 2
    for word in numbersWords:
        if word in text:
            firstWordPosition = text.find(word)
            if firstWordPosition < firstIndex:
                firstNumber = numbersWords[word]
                firstIndex = firstWordPosition

            lastWordPosition = text[::-1].find(word[::-1])
            if lastWordPosition < lastIndex:
                lastNumber = numbersWords[word]
                lastIndex = lastWordPosition     
        
    partTwo.append(firstNumber * 10 + lastNumber)

            
print(f"Part 1: {sum(partOne)}")
print(f"Part 2: {sum(partTwo)}")