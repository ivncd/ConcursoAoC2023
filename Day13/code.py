with open('input.txt', 'r') as f:
    data = f.read()

patterns = data.strip().split('\n\n')

def checkHorizontal(pattern : list, possibleStart : int) -> bool:
    minId = min(len(pattern) - (possibleStart + 2), possibleStart)
    isHorizontal = True
    for y in range(1, minId + 1):
        if pattern[possibleStart - y] != pattern[possibleStart + 1 + y]:
            isHorizontal = False
            break
    
    return isHorizontal

def checkVertical(pattern : list, possibleStart: int) -> bool:
    minId = min(len(pattern[0]) - (possibleStart + 2), possibleStart)
    isVertical = True
    for y in range(len(pattern)):
        if pattern[y][possibleStart - minId:possibleStart] != pattern[y][possibleStart + 2:possibleStart + 2 + minId][::-1]:
            isVertical = False
            break

    return isVertical

def getPatternResult(pattern : list, notAllowedResult : int = 0) -> int:
    result = 0
    for rowId in range(len(pattern) - 1):
        if pattern[rowId] == pattern[rowId + 1]:
            if checkHorizontal(pattern, rowId) and (rowId + 1) * 100 != notAllowedResult:
                result = (rowId + 1) * 100
                break
        
    else: 
        for columnId in range(len(pattern[0]) - 1):
            for y in range(len(pattern)):
                if pattern[y][columnId] != pattern[y][columnId + 1]:
                    break
            
            else:
                if checkVertical(pattern, columnId) and (columnId + 1) != notAllowedResult:
                    result = columnId + 1
                    break


    return result


resultPart1, resultPart2 = 0, 0
for pId, pattern in enumerate(patterns):
    pattern = pattern.splitlines()
    result1 = getPatternResult(pattern)
    
    resultPart1 += result1

    pattern = '\n'.join(pattern)
    for letterId in range(len(pattern)):
        newPattern = (pattern[:letterId] + ('.' if pattern[letterId] == '#' else ('#' if pattern[letterId] == '.' else pattern[letterId])) + pattern[letterId + 1:]).splitlines()
        result2 = getPatternResult(newPattern, result1)
        if result2 != 0: # Invalid pattern, no mirror
            break

    else: # In case there is no break in the loop then the smudge dont affect our solution so we just take the data
        result2 = result1
    
    resultPart2 += result2



print('Part 1:', resultPart1) #27502
print('Part 2:', resultPart2) #31947