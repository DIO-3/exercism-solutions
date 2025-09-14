# """Functions to help play and score a game of blackjack.

# How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
# "Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
# """


def value_of_card(card):
    if card in ["J", "Q", "K"]:
        return 10
    number_cards = ["2","3","4","5","6","7","8","9","10"]
    if card in number_cards:
        return int(card)
    if card == "A":
        return 1 

    # """Determine the scoring value of a card.

    # :param card: str - given card.
    # :return: int - value of a given card.  See below for values.

    # 1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    # 2.  'A' (ace card) = 1
    # 3.  '2' - '10' = numerical value.
    # """

    # pass

def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one > value_two:
        return card_one
    elif value_one < value_two:
        return card_two
    elif value_one == value_two:
        return card_one, card_two
    
    
    # """Determine which card has a higher value in the hand.

    # :param card_one, card_two: str - cards dealt in hand.  See below for values.
    # :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    # 1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    # 2.  'A' (ace card) = 1
    # 3.  '2' - '10' = numerical value.
    # """

    # pass

def value_of_ace(card_one, card_two):
    value_of_two_cards = value_of_card(card_one) + value_of_card(card_two)
    if card_one == "A" and card_one == card_two:
         return 12 
    elif value_of_two_cards > 10:
        return 1 
    elif value_of_two_cards <=3: 
        return 1
    elif value_of_two_cards <= 10:
        return 11 
    
    
    # """Calculate the most advantageous value for the ace card.

    # :param card_one, card_two: str - card dealt. See below for values.
    # :return: int - either 1 or 11 value of the upcoming ace card.

    # 1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    # 2.  'A' (ace card) = 11 (if already in hand)
    # 3.  '2' - '10' = numerical value.
    # """

    # pass

def is_blackjack(card_one, card_two):
    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)
    if value_of_card_one == 10 and value_of_card_two == 1:
        return True 
    elif value_of_card_one == 1 and value_of_card_two == 10:
        return True 
    else:
        return False 

    
    # """Determine if the hand is a 'natural' or 'blackjack'.

    # :param card_one, card_two: str - card dealt. See below for values.
    # :return: bool - is the hand is a blackjack (two cards worth 21).

    # 1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    # 2.  'A' (ace card) = 11 (if already in hand)
    # 3.  '2' - '10' = numerical value.
    # """

    # pass

def can_split_pairs(card_one, card_two):
    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)
    if value_of_card_one == value_of_card_two:
        print ("True")
        return True 
    else:
        print("False")
        return False    
    
    # """Determine if a player can split their hand into two hands.

    # :param card_one, card_two: str - cards dealt.
    # :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    # """

    # pass

def can_double_down(card_one, card_two):
    total_value = value_of_card(card_one) + value_of_card(card_two)
    if 9<= total_value <= 11:
        return True 
    else:
        return False
    
    # """Determine if a blackjack player can place a double down bet.

    # :param card_one, card_two: str - first and second cards in hand.
    # :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    # """

    # pass
