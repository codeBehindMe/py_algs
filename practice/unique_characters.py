# Given a string, check whether the characters are unique in a string.
# If the string is composed of all unique characters, return True, else False.
# Example:
#   "ABCD" -> True
#   "AABCDE" -> False


def check_unique(string: str):
    """
    Check's whether string is unique
    :param string:
    :return:
    """
    from collections import defaultdict
    d = defaultdict(int)
    for c in string:
        d[c] += 1
    if max(*d.values()) > 1:
        return False
    return True


if __name__ == '__main__':
    print(check_unique("abcdd"))
