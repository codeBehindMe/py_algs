# Check out the resources on the page's right side to learn more about arrays.
# The video tutorial is by Gayle Laakmann McDowell, author of the best-selling
# interview book Cracking the Coding Interview.
#
# A left rotation operation on an array shifts each of the array's elements
# unit to the left. For example, if  left rotations are performed on array ,
# then the array would become .
#
# Given an array  of  integers and a number, , perform  left rotations on the
# array. Return the updated array to be printed as a single line of
# space-separated integers.
from helpers import print_output


@print_output
def rot_left(a, d):
    """
    Given array and a number of pushes, rotates the elements in the array d
    indexes to the left.
    :param a: array
    :param d: rotations
    :return:
    """

    def rot_by_one(a: list):
        """
        Rotate the array by one
        :param a:
        :return:
        """
        first = a.pop(0)
        temp = a
        temp.append(first)

        return temp

    for i in range(d):
        temp = rot_by_one(a)

    return temp


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    d = 1

    rot_left(arr, d)
