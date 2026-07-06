def is_valid(isbn):
    total = 0
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    for index, digit in enumerate(isbn):
        if digit == "X":
            if index != 9:
                return False
            digit = 10
        elif digit.isdigit():
            digit = int(digit)
        else:
            return False

        value = digit * (10 - index)
        total += value

    return total % 11 == 0
    
        
