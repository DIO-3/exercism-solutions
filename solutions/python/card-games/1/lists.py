def get_rounds(number):
    rounds = [number, number+1, number+2]
    return rounds 

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2
    
def list_contains_round(rounds, number):
    if number in rounds: 
        return True 
    else:
        return False 

def card_average(hand):
    return sum(hand)/len(hand)
    
import statistics

def approx_average_is_average(hand):
    if (hand[0] + hand[-1]) / 2 == card_average(hand):
        return True
    elif statistics.median(hand) == card_average(hand):
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    even_number = hand[0::1]
    odd_number = hand[0::2]
    if card_average(even_number) == card_average(odd_number):
        return True 
    else:
        return False

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = hand[-1]*2
        return hand
    else:
        return hand  
