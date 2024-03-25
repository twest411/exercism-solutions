def square(number):
    i = 1
    if 1 <= number <= 64:
        while number != 1:
            i = 2 * i
            number -= 1
        return i
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    i = 64
    total = 0
    while i != 0:
        total += square(i)
        i -= 1
    return total
