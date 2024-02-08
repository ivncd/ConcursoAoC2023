with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip().splitlines()[:]
HANDS_AND_BETS = {line.split()[0] : int(line.split()[1]) for line in data}

def getCardValue(count):
    value = 1
    inverseCount = {}
    for card in count:
        times = count[card]
        if times in inverseCount:
            inverseCount[times].append(card)
        else:
            inverseCount[times] = [card]


    if 5 in inverseCount: # five
        value = 7
    elif 4 in inverseCount: # four
        value = 6
    elif 3 in inverseCount and 2 in inverseCount: # house
        value = 5
    elif 3 in inverseCount: # three
        value = 4
    elif 2 in inverseCount: # Double pair, one pair
        if len(inverseCount[2]) > 1:
            value = 3
        else:
            value = 2
    
    return value


def countCards(hand):
    cardCount = {}
    for letterId in range(len(hand)):
        letter = hand[letterId]
        if letter not in cardCount:
            cardCount[letter] = hand.count(letter)

    return cardCount

# Part 2
def transformForPart2(hand):
    if hand == 'JJJJJ': # Only case when you can't apply the code below
        return hand

    handWihoutJ = hand.replace('J', '')
    currentHighestValue, finalHand = 0, ''
    for letter in handWihoutJ:
        newHand = hand.replace('J', letter)
        cardCount = countCards(newHand)
        cardValue = getCardValue(cardCount)

        if cardValue > currentHighestValue:
            currentHighestValue, finalHand = cardValue, newHand
    
    return finalHand


def getOrder(part2 = False):
    orderByCardValue = {7 : [], 6 : [], 5 : [], 4 : [], 3 : [], 2 : [], 1 : []}
    cards = "23456789TJQKA" if not part2 else "J23456789TQKA"
    for hand in HANDS_AND_BETS:
        currentHand = hand

        # Part2 difference
        if part2 and 'J' in hand:
            currentHand = transformForPart2(hand)
        
        cardCount = countCards(currentHand) 
        cardValue = getCardValue(cardCount)
        if len(orderByCardValue[cardValue]) > 0:
            handAdded = False
            for rankId in range(len(orderByCardValue[cardValue])):
                if handAdded:
                    break

                rankedHand = orderByCardValue[cardValue][rankId]
                for cardId in range(len(rankedHand)):
                    rankedCard, card = rankedHand[cardId], hand[cardId]
                    if cards.index(card) == cards.index(rankedCard):
                        pass

                    elif cards.index(card) > cards.index(rankedCard):
                        orderByCardValue[cardValue].insert(rankId, hand)
                        handAdded = True
                        break

                    else:
                        break
                
                
            if not handAdded:
                orderByCardValue[cardValue].append(hand)
                
        else:
            orderByCardValue[cardValue].append(hand)

    return orderByCardValue


def result(order):
    result = 0
    rank = sum([len(order[key]) for key in order])
    for value in order:
        handList = order[value]
        for hand in handList:
            result += HANDS_AND_BETS[hand] * rank
            rank -= 1

    return result


# Part 1
orderByCardValue = getOrder()
resultPart1 = result(orderByCardValue)

# Part 2
orderByCardValue = getOrder(part2=True)
resultPart2 = result(orderByCardValue)


print(f"Part 1: {resultPart1}") # 250120186
print(f"Part 2: {resultPart2}") # 250665248
