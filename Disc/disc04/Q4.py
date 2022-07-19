def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if len(str(n)) == 2:
        if n % 10 + n // 10 == 10:
            return 1
        else:
            return 0
    return ten_pairs(int(str(n)[1:])) + count_digit(int(str(n)[1:]), 10 - int(str(n)[0]))
    # return ten_pairs(n % pow(10, len(str(n)) - 1)) + count_digit(n % pow(10, len(str(n)) - 1), 10 - n // pow(10, len(str(n)) - 1))


def count_digit(n, digit):
    """Return how many times digit appears in n.
    >>> count_digit(55055, 5)
    4
    >>> count_digit(12323, 2)
    2
    >>> count_digit(55055, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    cnt = 0
    for i in str(n):
        if str(digit) == i:
            cnt += 1
    # print(str(n) + " has " + str(cnt) + " of " + str(digit))
    return cnt

