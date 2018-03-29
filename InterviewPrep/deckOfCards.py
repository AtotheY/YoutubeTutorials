

def deckOfCards (deck):
    cardMap = {}
    # Storing The Cards
    for card in deck:
        if card not in cardMap:
            cardMap[card] = 1
        else:
            cardMap[card] += 1
    # Finding the card with the smallest count
    if len(cardMap) < 52:
        return 0
    return cardMap[min(cardMap, key=lambda k: cardMap[k])]


deck = ["AH,AS,5D,5D,AH"]
print deckOfCards(deck)