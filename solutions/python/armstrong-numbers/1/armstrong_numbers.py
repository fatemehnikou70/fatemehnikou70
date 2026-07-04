def is_armstrong_number(number):
    digits = str(number)
    power = len(digits)

    sum_of_powers = 0
    for d in digits:
        sum_of_powers += int(d) ** power

    return sum_of_powers == number