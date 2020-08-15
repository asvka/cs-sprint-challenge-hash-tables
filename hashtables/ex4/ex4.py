def has_negatives(a):
    # For an input list of integers, we wish to know which positive numbers
    # have corresponding negative numbers in the list.

    # same as ex3, create an empty dict and result
    array = {}
    result = []
    # iterate and add nums
    for i in a:
        if i not in array:
            array[i] = 1
    # check for negatives, second iteration?
    for i in a:
        if i > 0:
            if i * -1 in array:
                result.append(i)
    print(type(result))
    # return a list
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
