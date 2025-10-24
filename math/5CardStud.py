import random

def createDeck():
    deck = [];
    i = 0;
    while i < 52:
        deck.append(i);
        i += 1;
    return deck

def drawHand():
    hand = []
    rangenum = 51;
    numberOfCards = 5
    for i in range(numberOfCards):
        chosenIndex = random.randint(0,rangenum)
        hand.append(deck[chosenIndex])
        deck.pop(chosenIndex)
        rangenum -= 1
    return hand\
    
def checkSuit(hand):
    suits = []
    for card in hand:
        suit = card // 13
        suits.append(suit)
    return suits
    
def checkRank(hand):
    ranks = []
    for card in hand:
        rank = card % 13
        ranks.append(rank)
    return ranks

def checkStraight(ranks):
    if ranks[0] == ranks[1]-1 and ranks[1] == ranks[2]-1 and ranks[2] == ranks[3]-1 and ranks[3] == ranks[4]-1:
        return True
    else:
        return False
def checkFlush(suits):
    if suits[0] == suits[4]:
        return True
    else:
        return False
def checkRoyal(ranks):
    if ranks[0] == 0 and ranks[1] == 9 and ranks[2] == 10 and ranks[3] == 11 and ranks[4] == 12:
        return True
    else:
        return False

RoyalFlush = 0;
StraightFlush = 0;
FourOfAKind = 0;
FullHouse = 0;
Flush = 0;
Straight = 0;
ThreeOfAKind = 0;
TwoPair = 0;
Pair = 0;
Nothing = 0;

# Begin loop for a million
for i in range(1000000):
    deck = createDeck()
    hand = drawHand()
    suits = checkSuit(hand)
    ranks = checkRank(hand)
    suits.sort()
    ranks.sort()
    
    flush = checkFlush(suits)
    straight = checkStraight(ranks)
    royal = checkRoyal(ranks)

# Going through winning hands

    if flush and royal:
        RoyalFlush += 1
    elif flush and straight:
        StraightFlush += 1;
    elif ranks[0] == ranks [3] or ranks[1] == ranks[4]:
        FourOfAKind += 1;
    elif (ranks[0] == ranks[1] and ranks[2] == ranks[4]) or (ranks[0] == ranks[2] and ranks[3] == ranks[4]):
        FullHouse += 1;
    elif flush:
        Flush += 1;
    elif straight:
        Straight += 1;
    elif ranks[0] == ranks[2] or ranks[1] == ranks[3] or ranks[2] == ranks[4]:
        ThreeOfAKind += 1;
    elif (ranks[0] == ranks[1] and ranks[2] == ranks[3]) or (ranks[1] == ranks[2] and ranks[3] == ranks[4]) or (ranks[0] == ranks[1] and ranks[3] == ranks[4]):
        TwoPair += 1;
    elif (ranks[0] == ranks[1]) or (ranks[1] == ranks[2]) or (ranks[2] == ranks[3]) or (ranks[3] == ranks[4]):
        Pair += 1;
    else:
        Nothing += 1;

# End loop
print("Royal Flushes: ", RoyalFlush)
print("Straight Flushes: ", StraightFlush)
print("Four Of A Kind: ", FourOfAKind)
print("Full House: ", FullHouse)
print("Flushes: ", Flush)
print("Straights: ", Straight)
print("Three of a Kinds: ", ThreeOfAKind)
print("Two Pairs: ", TwoPair)
print("Pairs: ", Pair)
print("Nothing: ", Nothing)