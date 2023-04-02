# Blackjack Simulation
# Previously in this chapter you saw the card_dealer.py program that simulates cards being
# dealt from a deck. Enhance the program so it simulates a simplified version of the game of
# Blackjack between two virtual players. The cards have the following values:
# Numeric cards are assigned the value they have printed on them. For example, the value
# of the 2 of spades is 2, and the value of the 5 of diamonds is 5.
# Jacks, queens, and kings are valued at 10.
# Aces are valued at 1 or 11, depending on the player’s choice.
# The program should deal cards to each player until one player’s hand is worth more than 21 points. 
# When that happens, the other player is the winner. (It is possible that both players’ hands will 
# simultaneously exceed 21 points, in which case neither player wins.)
# The program should repeat until all the cards have been dealt from the deck.
# If a player is dealt an ace, the program should decide the value of the card according to the
# following rule: The ace will be worth 11 points, unless that makes the player’s hand exceed
# 21 points. In that case, the ace will be worth 1 point.

import random

def start():
    # Create a deck of cards.
    deck = create_deck()
    
    # Get the number of cards to deal.
    num_cards = int(input('How many cards should I deal? '))
    
    # Deal the cards.
    deal_cards(deck, num_cards)

    player1 = {'cards': [], 'score': 0}
    player2 = {'cards': [], 'score': 0}
    is_over = False
    while deck:
        deal(deck,player1)
        deal(deck,player2)
        if is_over:
            break
    get_winner(player1,player2)
 
# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3, 
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades':10,
            
            'Ace of Hearts':1, '2 of Hearts':2,'3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts':10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs':10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2,'3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}
    
    # Return the deck
    return deck

# The deal_cards function deals a specified number of cards
# from the deck.
def deal_cards(deck, number):
    # Initialize an accumulator for the hand value.
    hand_value = 0

    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck.
    if number > len(deck):
        number = len(deck)

    # Deal the cards and accumulate their values.
    for count in range(number):
        card = random.choice(list(deck))
        print(card)
        hand_value += deck[card]

    # Display the value of the hand.
    print(f'Value of this hand: {hand_value}')

def deal(deck,player):
    
    card = deck.popitem()
    if card == 'Ace of Spades' or card == 'Ace of Hearts' or card == 'Ace of Clubs' or card == 'Ace of Diamonds':
        if player['score'] + 11 <= 21:
            player['score'] += 11
        else:
            player['score'] += 1

    elif card in ['Jack of Spades','Queen of Spades', 'King of Spades','Jack of Hearts',
            'Queen of Hearts', 'King of Hearts','Jack of Clubs',
            'Queen of Clubs', 'King of Clubs','Jack of Diamonds',
            'Queen of Diamonds', 'King of Diamonds']:
        player['score'] += 10

    else:
        player['score'] += deck[card]
    player['cards'].append(card)

    if player['score'] > 21:
        print(f'{player["cards"]}-> GAME OVER')
        is_over = True

def get_winner(player1, player2):
    if player1['score'] <= 21 and (player2['score'] > 21 or player1['score'] > player2['score']):
        print(f'Player 1 wins with score {player1["score"]}')
    elif player2['score'] <= 21 and (player1['score'] > 21 or player2['score'] > player1['score']):
        print(f'Player 2 wins with score {player2["score"]}')
    else:
        print('No winner.')

start()
