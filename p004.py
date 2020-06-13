import itertools


def check_palindromic(num: int):
    '''
    Checks if a number is palindromic or not.
    :param num: The number to check if palindromic
    :return: Boolean. True if palindromic, False if not
    '''
    diglst = list(str(num)) # convert number to list of digits
    if diglst[::-1] == diglst:
        # if the list of numbers is exactly the same when reversed, it is palindromic
        return True
    else:
        return False


if __name__ == "__main__":
    # Create a list of all three-digit numbers
    numlst = list(range(100, 1000))

    # use itertools.combinations_with_replacement to generate list of all pairs of three-digit numbers
    # including cases where both numbers are the same
    # this will generate a list of tuples:
    # ie [ (100,100), (100, 101) ... (100, 999), (101, 102), (101, 103),... (999, 999)]
    # Since (105, 910) and (910, 105) are the same pair, and order doesn't matter, they are the same
    # The itertools.cominations_with_replacement function is smart and will not put these duplicates in
    pairs = list(itertools.combinations_with_replacement(numlst, 2))

    # Create a variable to store the value of the largest number (known so far) fitting the problems criteria
    maxnum = 0

    # For each pair in the list generatated by itertools.combinations_with_replacements
    # check if the product of the two numbers in that pair is palindromic.
    # If if is palindromic, test if it is the largest yet known palinrdome created as the product of 2 three-digit nums
    for tup in pairs:
        num = tup[0] * tup[1]
        if check_palindromic(num):
            maxnum = max(num, maxnum)

    # Print the largest number
    print(maxnum)
