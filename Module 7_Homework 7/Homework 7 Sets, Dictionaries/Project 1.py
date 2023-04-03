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

def main():
    count_round = 0
    player1_win = 0
    player2_win = 0
    no_win = 0
    both_win = 0

    # Create a deck of cards.
    deck = create_deck()
   
    while len(deck) != 0:
        hand_value1, hand_value2 = deal(deck)
        count_round += 1
        player1_winner, player2_winner, no_winner, both_winner = get_winner(hand_value1, hand_value2)
        if player1_winner:
            player1_win += 1
        elif player2_winner:
            player2_win += 1
        elif no_winner:
            no_win += 1
        else:
            both_win += 1

    print(f'Rounds played: {count_round}.\n')
    print(f'Player 1 wins {player1_win} rounds.\n')
    print(f'Player 2 wins {player2_win} rounds.\n')
    print(f'Both wins {both_win} round(s).\n')
    print(f'No wins {no_win} round(s).\n')

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

def deal(deck):
    hand_value1 = 0
    hand_value2 = 0

    while hand_value1 < 21 and hand_value2 < 21:
        card1 = random.choice(list(deck))
        print('Player 1:',card1)

        # Card of player 1
        if card1 == 'Ace of Spades' or card1 == 'Ace of Hearts'\
            or card1 == 'Ace of Clubs' or card1 == 'Ace of Diamonds':
            if hand_value1 + 11 > 21:
                hand_value1 += deck[card1]
                # remove key-value pair of player 1's card from the deck dictionary
                pop_card = deck.pop(card1)
            else:
                hand_value1 += 11
                pop_card = deck.pop(card1)
        else: 
            hand_value1 += deck[card1]
            pop_card = deck.pop(card1)

        if len(deck) == 0:
                break

        # Card of player 2
        card2 = random.choice(list(deck))
        print('Player 2:',card2)

        if card2 == 'Ace of Spades' or card2 == 'Ace of Hearts'\
            or card2 == 'Ace of Clubs' or card2 == 'Ace of Diamonds':
            if hand_value2 > 21:
                hand_value2 += deck[card2]
                # remove key-value pair of player 2's card from the deck dictionary
                pop_card = deck.pop(card2)
            else:
                hand_value2 += 11
                pop_card = deck.pop(card2)           
        else:
            hand_value2 += deck[card2]
            pop_card = deck.pop(card2)

        if len(deck) == 0:
            break
        
    return hand_value1, hand_value2

def get_winner(hand_value1,hand_value2):
    player1_winner = False
    player2_winner = False
    no_winner = False
    both_winner = False

    if hand_value1 <= 21 and hand_value2 > 21:
        print(f'Hand value of player 1: {hand_value1}.')
        print(f'Hand value of player 2: {hand_value2}.')
        print('Player 1 wins.\n')
        player1_winner = True
    elif hand_value1 > 21 and hand_value2 <= 21:
        print(f'Hand value of player 1: {hand_value1}.')
        print(f'Hand value of player 2: {hand_value2}.')
        print(f'Player 2 wins.\n')
        player2_winner = True
    elif hand_value1 > 21 and hand_value2 > 21:
        print(f'Hand value of player 1: {hand_value1}.')
        print(f'Hand value of player 2: {hand_value2}.')
        print('There is no winner.\n')
        no_winner = True
    else:
        print(f'Hand value of player 1: {hand_value1}.')
        print(f'Hand value of player 2: {hand_value2}.')
        print('Both players win.\n')
        both_winner = True
    return player1_winner, player2_winner, no_winner, both_winner
            
# Call the main function.
if __name__ == '__main__':
    main()
