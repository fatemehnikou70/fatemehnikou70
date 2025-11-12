def exchange_money(budget, exchange_rate):
    """
    Returns the value of the exchanged currency.
    
    :param budget: float - Amount of money to exchange
    :param exchange_rate: float - Rate of exchange (domestic per foreign)
    :return: float - Value after exchange
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Returns the remaining amount of money after exchanging.
    
    :param budget: float - Original budget
    :param exchanging_value: float - Money taken from budget to exchange
    :return: float - Remaining amount
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Returns the total value of the bills.
    
    :param denomination: int - Value of one bill
    :param number_of_bills: int - Number of bills
    :return: int - Total value
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    Returns the number of whole bills that fit into the amount.
    
    :param amount: float - Amount of money available
    :param denomination: int - Value of one bill
    :return: int - Number of whole bills
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """
    Returns the leftover amount that cannot be exchanged for whole bills.
    
    :param amount: float - Amount of money
    :param denomination: int - Value of one bill
    :return: float - Leftover amount
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Returns the maximum value of new currency after applying exchange rate, spread, and denomination constraints.
    
    :param budget: float - Amount of money to exchange
    :param exchange_rate: float - Base exchange rate
    :param spread: int - Percentage fee as integer
    :param denomination: int - Value of one bill
    :return: int - Maximum exchangeable value in whole bills
    """
    # Apply the spread to the exchange rate
    actual_rate = exchange_rate * (1 + spread / 100)
    # Calculate total foreign currency
    exchanged_amount = budget / actual_rate
    # Fit into whole bills only
    num_bills = get_number_of_bills(exchanged_amount, denomination)
    # Return the total value of the bills
    return get_value_of_bills(denomination, num_bills)
