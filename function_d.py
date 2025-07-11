def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    maxi = 0
    for i in range(len(numbers)):
        maxi = max(maxi, i)
    return maxi



if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
