# Given an integer array, output all the unique pairs that sum up to a
# specific value k.
# Example
#   Input: pairs_sum([1,3,2,2],4)
#   Output: (1,3) , (2,2)


def return_count(f):
    def wrapper_return_count(*args, **kwargs):
        return len(f(*args, **kwargs))

    return wrapper_return_count


@return_count
def pairs_sum(arr, target_sum):
    """
    Returns the pairs of numbers in the array which sum up to the target sum.
    Worse case runtime O(n^2)
    Best case runtime O(nLogn)
    :param arr:
    :param target_sum:
    :return:
    """
    # Container for output
    output = []
    # Linear scan and remove items that are greater than the target_sum.
    arr = [x for x in arr if x <= target_sum]

    # nLogN sort the values
    arr = sorted(arr)

    try:
        for i in range(len(arr)):
            for j in reversed(range(len(arr))):
                # Make sure that the indexes dont cross over.
                if i >= j:
                    raise StopIteration()
                if arr[i] + arr[j] > target_sum:
                    # If the right hand side is higher, then simply skip
                    # adding and move inwards from the right.
                    continue
                if arr[i] + arr[j] == target_sum:
                    # If the left and the right add up to the target sum, add
                    # the pair to the output then take the next item from the
                    # left.
                    output.append((arr[i], arr[j]))
                    break
                else:
                    # If it's less than that no point bringing the right in,
                    # just increment the left.
                    break
    except StopIteration:
        pass

    # Make the pairs unique and return.
    return list(set(output))


@return_count
def pairs_sum_linear(arr, target_sum):
    """
    A Linear implementation of the above.
    :param arr:
    :param target_sum:
    :return:
    """
    # If the array is less than size to, pairs are not possible.
    if len(arr) < 2:
        return []

    # Set's are great for making O(N^2) to O(n)
    # Keep a track of the values that we have seen
    seen = set()
    # Container for the actual output.
    output = set()

    # Traverse the list forward.
    for num in arr:
        # Compute the number that we would like to see in our list in order
        # to make a pair which would sum to the target_sum
        needed_val = target_sum - num

        if needed_val not in seen:
            # If the value that we need isn't been seen before, just add the
            # number we have seen and move on.
            seen.add(num)
        else:
            # If we have seen the number we would like then make a pair and
            # add it to the output.
            output.add((min(num, needed_val), max(num, needed_val)))

    return list(output)


if __name__ == '__main__':
    arr = [1, 2, 2, 3, 3]
    print(pairs_sum(arr, 4))
    print(pairs_sum_linear(arr, 4))
