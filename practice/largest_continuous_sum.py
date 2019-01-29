# Given an array of integers (positive and negative) find the largest
# continuous sum. Also report the start and endpoints of the sum
# Example:
#      [1,2,-2,3,4]
#   output:
#       (7, 3, 4)


def largest_continuous_sum(arr):
    """
    Computes the largest continuous sum.
    :param arr:
    :return:
    """
    if len(arr) == 0:
        return None
    m_sum = c_sum = arr[0]
    for num in arr[1:]:
        c_sum = max(num, c_sum + num)
        m_sum = max(c_sum, m_sum)
    return m_sum


if __name__ == '__main__':
    arr = [-1, -3, 1, 2, 3, -4, 1, 3, -2]

    print(largest_continuous_sum(arr))
