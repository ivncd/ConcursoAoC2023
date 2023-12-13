with open('input.txt', 'r') as f:
    data = f.read()


patterns = data.strip().split('\n\n')


def checkHorizontal(pattern, possibleStart):
    minId = min(len(pattern) - (possibleStart + 2), possibleStart)
    isHorizontal = True
    for y in range(1, minId + 1):
        if pattern[possibleStart - y] != pattern[possibleStart + 1 + y]:
            isHorizontal = False
            break
    
    return isHorizontal


def checkVertical(pattern, possibleStart):
    minId = min(len(pattern[0]) - (possibleStart + 2), possibleStart)
    isVertical = True
    for y in range(len(pattern)):
        if pattern[y][possibleStart - minId:possibleStart] != pattern[y][possibleStart + 2:possibleStart + 2 + minId][::-1]:
            isVertical = False
            break

    return isVertical


resultPattern = {}
resultPart1 = 0
for pId, pattern in enumerate(patterns):
    pattern = pattern.splitlines()
    for rowId in range(len(pattern) - 1):
        if pattern[rowId] == pattern[rowId + 1] and checkHorizontal(pattern, rowId):
            result = (rowId + 1) * 100
            break
        
    else: 
        for columnId in range(len(pattern[0]) - 1):
            for y in range(len(pattern)):
                if pattern[y][columnId] != pattern[y][columnId + 1]:
                    break
            
            else:
                if checkVertical(pattern, columnId):
                    result = columnId + 1
                    break
    
    resultPart1 += result
    resultPattern[pId] = result


"""
For later:

Refactor the code and create a function with the solving to not create another for in part2
"""

resultPart2 = 0
for pId, pattern in enumerate(patterns):
    lastResult = resultPart2
    for letterId in range(len(pattern)): # BRUTEFORCE PART 2
        newPattern = (pattern[:letterId] + ('.' if pattern[letterId] == '#' else ('#' if pattern[letterId] == '.' else pattern[letterId])) + pattern[letterId + 1:]).splitlines()
        for rowId in range(len(newPattern) - 1):
            if newPattern[rowId] == newPattern[rowId + 1]:
                if checkHorizontal(newPattern, rowId) and (rowId + 1) * 100 != resultPattern[pId]:
                    resultPart2 += (rowId + 1) * 100
                    break
            
        else:
            for columnId in range(len(newPattern[0]) - 1):
                for y in range(len(newPattern)):
                    if newPattern[y][columnId] != newPattern[y][columnId + 1]:
                        break
                
                else:
                    if checkVertical(newPattern, columnId) and ((columnId + 1)) != resultPattern[pId]:
                        resultPart2 += columnId + 1
                        break
        
        if resultPart2 > lastResult:
            break 
    
    else:
        resultPart2 += resultPattern[pId]



print('Part 1:', resultPart1)
print('Part 2:', resultPart2)