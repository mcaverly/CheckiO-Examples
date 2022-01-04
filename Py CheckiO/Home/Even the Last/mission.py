def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    sum_value = 0
    index = 0
    if len(array) > 0 and len(array) <= 20:
        for x in array:
            if index % 2 == 0:
                sum_value += x
                index += 1
                print(x, " ", array.index(x))
            elif index % 2 != 0:
                index += 1
        return sum_value * array[-1]
    elif len(array) == 0:
        return 0
    else:
        print("Invalid array")


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
