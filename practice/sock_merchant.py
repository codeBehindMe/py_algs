# John works at a clothing store. He has a large pile of socks that he must
# pair by color for sale. Given an array of integers representing the color of
# each sock, determine how many pairs of socks with matching colors there are.
# For example, there are  socks with colors . There is one pair of color  and
# one of color . There are three odd socks left, one of each color. The number
# of pairs is .
# FIXME: Description
from helpers import print_output


@print_output
def count_pairs(n: int, ar: iter):
    from collections import defaultdict

    d = defaultdict(int)

    for s in ar:
        d[s] += 1

    return sum([x // 2 for x in d.values()])


if __name__ == '__main__':
    n = 9
    socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    count_pairs(n, socks)
