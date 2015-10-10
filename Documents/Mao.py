from random import shuffle
class Card:
    def __init__(self,suit,number):
        self.suit=suit
        self.number=number
        
    def __str__(self):
        return str(self.number)+" of "+self.suit

class Deck:
    def __init__(self):
        self.deck=[]
        for i in range(13):
            self.deck.append(Card('heart',i+1))
            self.deck.append(Card('spades',i+1))
            self.deck.append(Card('diamond',i+1))
            self.deck.append(Card('clubs',i+1))
  
    def __str__(self):
        v=""
        for i in self.deck:
            v+=str(i.number)+" of "+str(i.suit)+"\n"
        return v
            
    def shuffle_deck(self):
        rand_ints=(list(range(52)))
        shuffle(rand_ints)
        rand_deck=[self.deck[rand_ints[i]] for i in range(len(rand_ints))]
        self.deck=rand_deck
    
    def create_hand(self):
        """
        Adds a given number of cards to a Player's hand
        """
        new_hand=[]
        num_cards_given=5
        for i in range(num_cards_given):
            new_hand.append(self.deck[0])
            self.deck.remove(self.deck[0])
        return new_hand
        
    def draw(self,player):      
        """
        Adds the top card of the deck(self) to the Player's hand
        
        >>> deck=Deck()
        >>> player0=Player()
        >>> deck.draw(player0)
        >>> print(player0)
        1 of heart
        """
        next_card = self.deck[0]
        player.hand.append(next_card)
        self.deck.remove(next_card)
        

class Player:
    def __init__(self, name):
        self.hand=[]
        self.turn=0
        self.name=name
        self.is_user=True

    def __str__(self):
        blah=""
        i=0
        for card in self.hand:
            i+=1
            blah+="("+str(i)+") "+str(card)+" "
        return blah
    
    def __len__(self):
        return len(self.hand)
        
    def play_card(self,deck):
        print("Below is player "+self.name+"'s hand")
        print(self)
        index_of_wanted_card=int(input("PLAYER "+self.name+":Enter the index of the card you want to play. Enter 0 if you want to draw a card."))
        if(index_of_wanted_card==0):
            deck.draw(self)
            return None
        wanted_card=self.hand[index_of_wanted_card-1]
        self.hand.remove(self.hand[index_of_wanted_card-1])
        return wanted_card
        
def playgame(num_players):
    players=[]
    for i in range(num_players):
        person_name=input("Enter Your Name Here:")
        players.append(Player(person_name))
    deck=Deck()
    deck.shuffle_deck()
    for player in players:
        if player.turn==0:
            player.hand=deck.create_hand()
    face_up_card=deck.deck[0]
    deck.deck.remove(deck.deck[0])
    #makes sure all players have hands of at least 1 card in their hand
    while(min([len(player) for player in players]) != 0):
        for player in players:
            print("Current Card: "+str(face_up_card))
            face_up_card=take_turn(face_up_card,player,deck)
            if(len(player)==0):
                print(player.name+" WINS THE GAME!!")
                break

def take_turn(face_up_card,player,deck):
    temp_card=player.play_card(deck)
    if(temp_card==None):
        return face_up_card
    if action(face_up_card, temp_card, player)==False:
        print("PLAY A LEGAL CARD")
        deck.draw(player)
        player.hand.append(temp_card)
        return take_turn(face_up_card, player, deck)
    else:
        return temp_card
        
def isValidMove(current_card, played_card):
    if(current_card.suit==played_card.suit or current_card.number == played_card.number):
        return True
    else:
        return False
def isSeven(card):
    return card.number == 7
def isSpade(card):
    return card.suit == 'spades'
def action(current_card, played_card, player):
    if isValidMove(current_card, played_card)==False:
        return False
    else: 
        if isSeven(played_card):
            print('is seven')
            return True
        if isSpade(played_card):
            print('is spade')
            return True
    # def thank_you(card):

    # def last_card():

    # def end_game

    # def cannot_play(card):
"""
class extraRules(Rules):
    # to be implemented when player wins 
    def isPrime(card):
        primeNumbers = [2,3,5,7,11,13]
        return card.number in primeNumbers
    def isEven(card):
        return card.number%2 == 0
"""
