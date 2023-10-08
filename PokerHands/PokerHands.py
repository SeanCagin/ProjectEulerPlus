# we convert the hand the user enters into an array that is easy to compare
# it follows this format: [value of hand, most repeating card, second most repeating card, other cards]
# if two cards repeat the same amount, they are entered in decsending order
# the following lists the value of each hand:
# straight flush = 8, four of a kind = 7, full house = 6, flush = 5, straight = 4
# three of a kind = 3, two pair = 2, single pair = 1, high card = 0


from operator import itemgetter
   

class Poker_Hand:
    class Card:
        def __init__(self, rawData):
            # raw data is a string like 5C or KH - card value, card suit
            self.value = self.getCardValue(rawData[0])
            self.suit = self.getCardValue(rawData[1])

        def getCardValue(self, c):  # converts both card face/value and suit to a number
            if (ord(c) < 65):  # if c is between 2-9 return that value
                return int(c)
            conversion = {
                "T": 10,
                "J": 11,
                "Q": 12,
                "K": 13,
                "A": 14,
                "C": 0,  # clubs
                "D": 1,  # diamonds
                "H": 2,  # hearts
                "S": 3   # spades
            }
            return conversion.get(c)
        
        def getValue(self):
            return self.value
        
        def getSuit(self):
            return self.suit


    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

    SIZE = 5

    REPEAT_VALUE = 0
    REPEAT_COUNT = 1

    def __init__(self, hand):  # Hand is the set of 5 cards one has
        self.hand = self.processRawHand(hand)
        
    
    def processRawHand(self, raw):
        processedHand = []
        for i in range(0, len(raw)):
            processedHand.append(self.Card(raw[i]))
        return processedHand
   
    
    def compare(self, hand2):
        equiv1 = self.convert()  # equivalent comparable array of hand1
        equiv2 = hand2.convert()  # equivalent comparable array of hand2
        traverser = 0
        while (traverser < self.SIZE):
            if (traverser == len(equiv1)):
                return 0  # Neither player wins
            if (equiv1[traverser] > equiv2[traverser]):
                return 1  # Player one wins
            elif (equiv1[traverser] == equiv2[traverser]):
                traverser += 1
            else:
                return -1  # player two wins
      
      
    def convert(self):
        self.pokerSort()
        if (self.allSuitSame()):  # we seperate flushes from non-flushes
            return self.straightArray(self.STRAIGHT_FLUSH, self.FLUSH) 
        return self.convertDiffSuit()
            

    def convertDiffSuit(self):
        repeats = self.getRepeats()
        if (len(repeats) == 0):  # either a high-card hand or a straight
            return self.straightArray(self.STRAIGHT, self.HIGH_CARD) 
            
        if (repeats[0][self.REPEAT_COUNT] == 4):  # four of a kind
            return [self.FOUR_OF_A_KIND, repeats[0][self.REPEAT_VALUE]]
        
        if (repeats[0][self.REPEAT_COUNT] == 3):  # three of a kind or full house
            return self.threeRepArray(repeats)
            
        if (len(repeats) == 1):  # pair
            return self.pairArray(repeats)

        return self.twoPairArray(repeats)  # we have checked every case but two pair
    
    
    def twoPairArray(self, repeats):
        retval = [2, repeats[0][self.REPEAT_VALUE], repeats[1][self.REPEAT_VALUE]]
        for i in range(0, self.SIZE): # adds the only non-repeating card as a tie-breaker
            if (self.hand[i].getValue() != repeats[0][self.REPEAT_VALUE] and self.hand[i].getValue() != repeats[1][self.REPEAT_VALUE]):
                retval.append(self.hand[i].getValue())
        return retval
        
        
    def pairArray(self, repeats):
        retval = [1, repeats[0][self.REPEAT_VALUE]]
        for i in range(0, self.SIZE):
            if (self.hand[i].getValue() != repeats[0][self.REPEAT_VALUE]):
                retval.append(self.hand[i].getValue())
        return retval
        
        
    def threeRepArray(self, repeats):
        if (len(repeats) == 1):  # 3 of a kind, returns [3, repeat card, higher card, lower card]
            retval = [3, repeats[0][self.REPEAT_VALUE]]
            for i in range(0, self.SIZE):
                if (self.hand[i].getValue() != repeats[0][self.REPEAT_VALUE]):
                    retval.append(self.hand[i].getValue())
            return retval
            
        return [6, repeats[0][self.REPEAT_VALUE], repeats[1][self.REPEAT_VALUE]]  # full house, returns [6, 3 repeat card, 2 repeat card]
        

    # for flush trueWeight = 8 (straight), falseweight = 5 (not straight), for non-flush trueweight = 4 (straight), falseweight = 0 (not straight)    
    def straightArray(self, trueWeight, falseWeight): 
        straightVal = self.isStraight()
        if (straightVal == 1):
            return [trueWeight, self.hand[0].getValue()]  # highest card of the straight5
            
        elif (straightVal == 2):
            return [trueWeight, self.hand[1].getValue()]  # 14-5-4-3-2 (A2345)
            
        retval = [falseWeight]
        for i in range(0, self.SIZE):
            retval.append(self.hand[i].getValue())
        return retval
        
        
    def isStraight(self):  # 0 = no straight, 1 = normal straight, 2 = wheel straight
        for i in range(0, self.SIZE-1):
            case1 = self.hand[i].getValue() == self.hand[i+1].getValue()+1  # regular straight
            case2 = i == 0 and self.hand[i].getValue() == self.hand[i+1].getValue()+9  # 14, 5, 4, 3, 2
            if (not case1 and not case2):
                return 0
        
        if (self.hand[0].getValue() == self.hand[1].getValue()+9):
            return 2
        return 1

            
    def getRepeats(self):  # Cases: 4, 3-2, 3, 2-2, 2
        repeats = []
        count = 1
        for i in range(0, self.SIZE):
            if (i != self.SIZE-1 and self.hand[i].getValue() == self.hand[i+1].getValue()):
                count += 1
            elif (count > 1):
                if (count > 2):  # Cases: 4, 3-2, 3
                    repeats.insert(0, [self.hand[i].getValue(), count])
                elif (count == 2):  # Cases: 2-2, 2
                    repeats.append([self.hand[i].getValue(), count])
                count = 1
                        
        return repeats
        
                                
    def pokerSort(self):  # Returns list sorted in descending order by card value
        self.hand = sorted(self.hand, key=lambda h: h.getValue(), reverse=True)


    def allSuitSame(self):  # Checks if all cards in a hand have the same suit
        for i in range(0, self.SIZE-1):
            if (self.hand[i].getSuit() != self.hand[i+1].getSuit()):
                return False
        return True
    
    
    def __str__(self):
        return str(self.hand)
    


# ------------------- Program begins here -------------------
caseCount = int(input())
for i in range(0, caseCount):
    line = input().split()
    rawHand1 = line[0:5]
    rawHand2 = line[5:]
    h1 = Poker_Hand(rawHand1)  # Gets the first 15 chars which is the first hand
    h2 = Poker_Hand(rawHand2)
    if (h1.compare(h2) == 1):
        print("Player 1")
    else:
        print("Player 2")
    