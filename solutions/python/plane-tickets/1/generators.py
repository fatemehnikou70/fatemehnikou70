"""Functions to automate Conda airlines ticketing system."""
#1
def generate_seat_letters(number):
    
    letters = ["A", "B", "C", "D"]

    for i in range(number):
        yield letters[i % 4]

    
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    pass
#2
def generate_seats(number):
    letters = "ABCD"
    row = 1
    seat = 0

    while seat < number:

        # اگر رسیدیم به ردیف 13، ردش کن
        if row == 13:
            row += 1
            continue

        # انتخاب حرف صندلی (A, B, C, D)
        letter = letters[seat % 4]

        # ساختن شماره صندلی مثل 3A
        yield f"{row}{letter}"

        seat += 1

        # هر 4 صندلی برو ردیف بعدی
        if seat % 4 == 0:
            row += 1
            
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    pass


#3
def assign_seats(passengers):
    letters = "ABCD"
    seats = {}
    row = 1
    seat_index = 0

    for name in passengers:

        # رد کردن ردیف 13
        if row == 13:
            row += 1

        # انتخاب حرف صندلی
        letter = letters[seat_index % 4]

        # ساختن شماره صندلی مثل 2B
        seats[name] = f"{row}{letter}"

        seat_index += 1

        # هر 4 نفر برو ردیف بعدی
        if seat_index % 4 == 0:
            row += 1

    return seats
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    pass


#4
def generate_codes(seat_numbers, flight_id):
    for i, seat in enumerate(seat_numbers):
        code = seat + flight_id + "000"
        if len(code) > 12:
            code = code[:12]
        yield code
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    pass
