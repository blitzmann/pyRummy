class RunError(ValueError): pass
class SetError(ValueError): pass

class Meld(object):
    #@todo: use contants for types
    def __init__(self):
        self.cards   = []
        self.end     = False

    def checkEnd(self):
        '''check to see if meld has ended'''
        '''this will only check cards currently on table'''
        '''This may or may not be implemented (see: Table class)'''
    
class RunMeld(Meld):
    def __init__(self, cards):
        super().__init__()
        # Add initial batchs of cards
        self.add(cards)
        
    def add(self, cards):
        '''
            Verify and add cards to run
            
            First we create a test list that include the cards currently in Meld, 
            and also the (potentially invalid) cards that we want to add. We sort 
            and pass this list along to some testing functions
        '''
        tempCards = self.cards + cards
        tempCards.sort(key=lambda x: x.rank)
        self.checkSuit(tempCards)
        self.checkSeq(tempCards)
        
        # If we got here, it all checks out. Reassign cards in Meld
        self.cards = tempCards

    def checkSeq(self, cards):
        '''
            Check sequence of Run.
            
            This functions takes in a list of Cards and then checks for proper 
            sequencing. The following equation is used to check:
            
            (RankHigh - RankLow) == (#Cards - 1)
            
            Since a sequence would always result in this equation being true, if 
            it returns false then that means there is either an Ace low or a 
            broken sequence
        '''
        if cards[-1].rank - cards[0].rank is not len(cards) - 1:
        
            # sequence error or low ace
            if cards[-1].rank == 14:
            
                # could be low ace, need to modify cards list and retest
                cards[-1].rank = 1           # set Ace to rank 1
                cards.insert(0, cards.pop()) # Move Ace to bottom of list
                
                if cards[-1].rank - cards[0].rank is not (len(cards)-1):
                
                    # still doesn't work, sequence error, return ACE to rank 14
                    cards[0].rank = 14 
                    raise RunError('Broken Sequence')
            else:
                raise RunError('Broken Sequence')
        
    def checkSuit(self, cards):
        '''
            This function simply checks to make sure our test cards have only 1
            suit by using set()
        '''
        if len(set(x.suitIndex for x in cards)) is not 1:
            raise RunError('Invalid Suit')

class SetMeld(Meld):
    def __init__(self, cards):
        super().__init__()
        # Add initial batchs of cards
        self.add(cards)
        
    def add(self, cards):
        '''Verify and add cards to set'''
        tempCards = self.cards + cards
        tempCards.sort(key=lambda x: x.suitIndex)
        self.checkFace(tempCards)
        self.checkSuit(tempCards)
        
        # If we got here, it all checks out. Reassign cards in Meld
        self.cards = tempCards

    def checkSuit(self, cards):
        '''Checks to make sure if suit does not exist yet in set'''
        found = set()
        for c in cards:
            if c.suitIndex in found:
                raise SetError('Duplicate Suit')
            else:
                found.add(c.suitIndex)
            
    def checkFace(self, cards):
        '''
            This function simply checks to make sure our test cards have only 1
            rank by using set()
        '''
        if len(set(x.rank for x in cards)) is not 1:
            raise SetError('Invalid Rank')
                