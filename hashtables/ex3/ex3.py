def intersection(arrays):
    # Find the intersection between multiple lists of integers.
    array = {}
    result = []

    for i in arrays:
        for num in i:
            if num not in array:
                array[num] = 1
            else:
                result.append(num)
    # Return a list
    result = list(dict.fromkeys(result))
    return result




if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
