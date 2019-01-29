# Consider an array of non-negative integers. A second array is formed by
# shuffling the elements of the first array and deleting a random element.
# Given these two arrays, find which element is missing from the second array.
# Example:
#      Arr1: [1,2,3,4,5,6,7]
#      Arr2: [4,3,2,6,7,1]
# Missing element is 5.


def find_missing_element(arr1, arr2):
    """
    Finds the missing element in arr2 given arr1.
    Complexity is O(N)
    This is vulnerable to numerical overflow and underflow.
    :param arr1:
    :param arr2:
    :return:
    """
    return sum(arr1) - sum(arr2)


def find_missing_element_sorted(arr1, arr2):
    """
    Sorted version of the missing element.
    Complexity is O(nlogn)
    :param arr1:
    :param arr2:
    :return:
    """

    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    for a, b in zip(arr1, arr2):
        if a != b:
            return a


def find_missing_element_hashtable(arr1, arr2):
    """
    Hashtable version of the missing element.
    Complexity is O(n)
    :param arr1:
    :param arr2:
    :return:
    """
    from collections import defaultdict

    d = defaultdict(int)

    for n in arr2:
        d[n] += 1

    for n in arr1:
        if d[n] == 0:
            return n
        else:
            d[n] -= 1


def find_missing_element_xor(arr1, arr2):
    """
    Exclusive or for finding the missing element.
    :param arr1:
    :param arr2:
    :return:
    """
    result = 0

    arr_t = arr1 + arr2
    for num in arr_t:
        result ^= num

    return result


if __name__ == '__main__':
    assert find_missing_element([5, 5, 7, 7], [5, 7, 7]) == 5
    assert find_missing_element([1, 2, 3, 4, 5, 6, 7],
                                [3, 7, 2, 1, 4, 6]) == 5
    assert find_missing_element([9, 8, 7, 6, 5, 4, 3, 2, 1],
                                [9, 8, 7, 5, 4, 3, 2, 1]) == 6

    assert find_missing_element_sorted([5, 5, 7, 7], [5, 7, 7]) == 5
    assert find_missing_element_sorted([1, 2, 3, 4, 5, 6, 7],
                                       [3, 7, 2, 1, 4, 6]) == 5
    assert find_missing_element_sorted([9, 8, 7, 6, 5, 4, 3, 2, 1],
                                       [9, 8, 7, 5, 4, 3, 2, 1]) == 6

    assert find_missing_element_hashtable([5, 5, 7, 7], [5, 7, 7]) == 5
    assert find_missing_element_hashtable([1, 2, 3, 4, 5, 6, 7],
                                          [3, 7, 2, 1, 4, 6]) == 5
    assert find_missing_element_hashtable([9, 8, 7, 6, 5, 4, 3, 2, 1],
                                          [9, 8, 7, 5, 4, 3, 2, 1]) == 6

    assert find_missing_element_xor([5, 5, 7, 7], [5, 7, 7]) == 5
    assert find_missing_element_xor([1, 2, 3, 4, 5, 6, 7],
                                    [3, 7, 2, 1, 4, 6]) == 5
    assert find_missing_element_xor([9, 8, 7, 6, 5, 4, 3, 2, 1],
                                    [9, 8, 7, 5, 4, 3, 2, 1]) == 6
