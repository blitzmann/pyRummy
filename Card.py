import random

class Card():
    suitNames = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
    faceNames = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
 
    def __init__(self, str='AS'):
        
        '''
            Card class defines one card
            
            Initialize with a string in this format: 10S (10 of Spades)
        '''
        
        # start conversion of human-readable string to proper indexs
        n = len(str) 
        face, suit = str[0:n-1], str[n-1:n]
        
        for i in range(0, 4):
            if self.suitNames[i][0] == suit:
                suit = i
                break
        
        if face.isdecimal() is True:
            face = int(face) - 2 # index of given face value
        else:
            for i in range(9, 13):
                if self.faceNames[i][0] == face:
                    face = i
                    break
                    
        self.suitIndex = suit
        self.faceIndex = face   
        self.rank      = face + 2
    
    def __int__(self):
        return self.rank
    
    def suitName(self):
        return Card.suitNames[self.suitIndex]

    def faceName(self):
        return Card.faceNames[self.faceIndex]
        
    def isFace(self, face):
        return Card.faceNames[self.faceIndex] == face
    
    def isSuit(self, suit):
        return Card.suitNames[self.suitIndex] == suit

    def __str__(self):
        return "%s of %s" % (self.faceName(), self.suitName())

class Deck():
    
    '''
        Deck handles building cards into decks, or alternatively returning
        specific runs / sets for test cases
    '''
    
    def __init__(self):
        self.cards = []
        for suit in Card.suitNames:
            for face in Card.faceNames:
                if face.isdecimal() is True:
                    self.cards.append(Card(face+suit[0]))
                else:
                    self.cards.append(Card(face[0]+suit[0]))

    def show(self):
        for i in range(len(self.cards)):
            print("%d\t %s" % (i+1, self.cards[i]))

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, n):
        res, self.cards = self.cards[:n], self.cards[n:]
        return res
       
    def makeRun(suit):
        run = []
        for face in Card.faceNames:
            if face.isdecimal() is True:
                run.append(Card(face+suit))
            else:
                run.append(Card(face[0]+suit))
        return run
    
    def makeSet(face):
        set = []
        for suit in Card.suitNames:
            set.append(Card(face+suit[0]))
        return set