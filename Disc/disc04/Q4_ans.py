def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    if n < 10:
        return 0
    else:
        return ten_pairs(n//10) + count_digit(n//10, 10 - n%10)

def count_digit(n, digit):
    """Return how many times digit appears in n.
    >>> count_digit(55055, 5)
    4
    """
    if n == 0:
        return 0
    else:
        if n%10 == digit:
            return count_digit(n//10, digit) + 1
        else:
            return count_digit(n//10, digit)