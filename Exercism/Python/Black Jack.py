def value_of_card(card):
    
    values_of_card = { "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10 }

    return values_of_card[card]
    


def higher_card( card_one, card_two ):
    
    difference = value_of_card( card_one ) - value_of_card( card_two )

    if difference > 0:
        return card_one

    if difference < 0:
        return card_two

    return ( card_one, card_two )
    


def value_of_ace(card_one, card_two):
    
    score = value_of_card( card_one ) + value_of_card( card_two )

    if score > 10 or card_one == "A" or card_two == "A":
        return 1

    return 11
    


def is_blackjack( card_one, card_two ):
    
    score = value_of_card( card_one ) + value_of_card( card_two )

    return score == 11 and ( card_one == "A" or card_two == "A" )
    


def can_split_pairs( card_one, card_two ):

    return card_one == card_two or card_one in "QK" and card_two in "QK"
    


def can_double_down( card_one, card_two ):
    
    score = value_of_card( card_one ) + value_of_card( card_two )
    
    return score > 8 and score < 12
