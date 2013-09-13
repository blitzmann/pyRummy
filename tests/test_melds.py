from pyRummy.Meld import RunError, SetError
from pyRummy.Meld import Meld, RunMeld, SetMeld
from pyRummy.Card import Card, Deck
import unittest

class MeldTestCase(unittest.TestCase):
    def setUp(self):
        '''set up test cases for all Meld tests'''
        self.run  = Deck.makeRun('C') # a full run of Clubs
        self.set  = Deck.makeSet('10') # a full set of 10's
        self.deck = Deck() # 52 card deck (non-shuffled)

class MeldRun(MeldTestCase):               
    '''test normal case scenerios'''
    def setUp(self): 
        '''sets up test case for runs by starting off with 4-5-6 of Clubs'''
        MeldTestCase.setUp(self)
        self.initCards = [Card('4C'), Card('5C'), Card('6C')]

        self.Meld = RunMeld(self.initCards) # init run meld

    def test_initilize(self):           
        '''tests if Meld inits Run properly and adds cards.'''
        self.assertEqual(self.Meld.cards, self.initCards)

    def test_add(self):
        '''test normal additions'''
        cards = [Card('3C'), Card('7C')] # 3 and 7 of Clubs
        self.Meld.add(cards)

        # check to make sure first and last card in Meld are the cards we added
        self.assertEqual(self.Meld.cards[-1], cards[1])
        self.assertEqual(self.Meld.cards[0], cards[0])

    def test_end(self):
        '''end the run, and test to make sure cards cannot be added to it'''
        '''This may or may not be implemented (see: Table class)'''
        
    def test_aces(self):
        '''test automatic determination of Ace high'''
        
        # Add Aces low to test case
        cards = [Card('AC'), Card('2C'), Card('3C')]
        self.Meld.add(cards)
        
        self.assertEqual(self.Meld.cards[0].rank, 1)
        self.assertEqual(self.Meld.cards[-1].rank, 6)
        
        # Add rest of suit, make sure Ace remains low
        cards = [Card('7C'), Card('8C'), Card('9C'), \
                 Card('10C'), Card('JC'), Card('QC'), Card('KC')]
                 
        self.Meld.add(cards) 
        
        self.assertEqual(self.Meld.cards[0].rank, 1)
        self.assertEqual(self.Meld.cards[-1].rank, 13)
        
        # Remove Ace and 2, then re-add, making sure Ace is high 
        del self.Meld.cards[0:2]
        self.Meld.add([Card('AC'), Card('2C')])
                
        self.assertEqual(self.Meld.cards[0].rank, 2)
        self.assertEqual(self.Meld.cards[-1].rank, 14)
        
        # remove Ace, re-add to simulate Aces high with 2C already in deck
        self.Meld.cards.pop()
        self.Meld.add([Card('AC')])
        
        self.assertEqual(self.Meld.cards[0].rank, 2)
        self.assertEqual(self.Meld.cards[-1].rank, 14)            

class MeldBadRun(MeldTestCase): 
    '''tests to check bad input for Runs'''
    def setUp(self): 
        MeldTestCase.setUp(self)
        self.initCards = [Card('4C'), Card('5C'), Card('6C')]

        self.Meld = RunMeld(self.initCards) # init run meld
        
    def test_suit(self): 
        '''test for proper suit'''
        self.assertRaises(RunError, self.Meld.add, [Card('7C'),Card('3H')])

    def test_continuation(self): 
        '''test for proper continuation'''
        self.assertRaises(RunError, self.Meld.add, [Card('9C'),Card('2C'),Card('JC')])
        self.assertRaises(RunError, self.Meld.add, [Card('7C'),Card('8C'),Card('10C')])

    def test_unique(self):
        '''test for uniquness of card in run'''
        self.assertRaises(RunError, self.Meld.add, [Card('4C'),Card('5C')])

class MeldSet(MeldTestCase):               
    '''test normal case scenerios'''
    
    def setUp(self): 
        '''sets up test case for sets by starting off with 10's (Clubs missing)'''
        MeldTestCase.setUp(self)
        self.initCards = [Card('10H'), Card('10S'), Card('10D')]
        # Sets are sorted in the following order when added: DCHS
        self.Meld = SetMeld(self.initCards) # init set meld

    def test_initilize(self):           
        '''tests if Meld inits Set properly and adds/sorts cards.'''
        self.assertEqual(self.Meld.cards[0], self.initCards[2])
        self.assertEqual(self.Meld.cards[1], self.initCards[0])
        self.assertEqual(self.Meld.cards[2], self.initCards[1])

    def test_add(self):
        '''test normal additions'''
        cards = [Card('10C')]
        self.Meld.add(cards)

        # check to make sure sort was correct
        self.assertEqual(self.Meld.cards[0], self.initCards[2])
        self.assertEqual(self.Meld.cards[1], cards[0])
        self.assertEqual(self.Meld.cards[2], self.initCards[0])
        self.assertEqual(self.Meld.cards[3], self.initCards[1])

class MeldBadSet(MeldTestCase): 
    '''tests to check bad input for Sets'''
    def setUp(self): 
        MeldTestCase.setUp(self)
        self.initCards = [Card('10H'), Card('10S'), Card('10D')]

        self.Meld = SetMeld(self.initCards) # init run meld
        
    def test_suit(self): 
        '''test for valid suit'''
        self.assertRaises(SetError, self.Meld.add, [Card('10S')])

    def test_face(self): 
        '''test for proper face value'''
        self.assertRaises(SetError, self.Meld.add, [Card('9C')])

         
if __name__ == '__main__':
    unittest.main()