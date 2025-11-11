def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)
    if v1 > v2:
        return card_one
    elif v2 > v1:
        return card_two
    else:
        return (card_one, card_two)


def value_of_ace(card_one, card_two):
    v1 = 11 if card_one == 'A' else value_of_card(card_one)
    v2 = 11 if card_two == 'A' else value_of_card(card_two)
    if v1 + v2 + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    return (
        ('A' in [card_one, card_two]) and
        (value_of_card(card_one) + value_of_card(card_two) == 11)
    )


def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]
