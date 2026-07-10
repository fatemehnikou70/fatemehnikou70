def sum_of_multiples(limit, multiples):
    numbers = set()

    for number in range(1, limit):
        for multiple in multiples:
            if multiple == 0:
                continue
            if number % multiple == 0:
                numbers.add(number)

    return sum(numbers)