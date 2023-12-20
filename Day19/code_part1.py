with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip()
workflows, ratings = data.split('\n\n')[0].splitlines(), data.split('\n\n')[1].splitlines()

# Handle Workflow Data
workflowDict = {}
for workflow in workflows:
    id, follows = workflow.split('{')[0], workflow.split('{')[1][:-1].split(',')
    workflowDict[id] = []
    follows, other = follows[:-1], follows[-1]
    for follow in follows:
        variable, symbol = follow[0] ,follow[1]
        number, next = int(follow[2:].split(':')[0]), follow[2:].split(':')[1] 
        workflowDict[id].append((variable, symbol, number, next))
    
    workflowDict[id].append(other)

# Handle ratings
ratingsList = []
for rating in ratings:
    ratingDict, allRatings = rating[1:-1].split(','), {}
    for r in allRatings:
        variable, number = r.split('=')[0], int(r.split('=')[1])
        ratingDict[variable] = number
    
    ratingsList.append(ratingDict)


def isValue(value, variableData):
    if variableData[1] == '<':
        return value < variableData[2]
    else:
        return value > variableData[2]


resultPart1 = 0
for rating in ratingsList:
    currentWorkflow = "in"
    while currentWorkflow not in ('A', 'R'):
        for workflow in workflowDict[currentWorkflow][:-1]:
            for variable in rating:
                if variable == workflow[0]:
                    if isValue(rating[variable], workflow):
                        currentWorkflow = workflow[-1]
                        break
            
            else:
                continue

            break
   
        else:
            currentWorkflow = workflowDict[currentWorkflow][-1]
        
    if currentWorkflow == 'A':
        resultPart1 += sum(rating.values())
    

print('Part 1:', resultPart1) # 509597