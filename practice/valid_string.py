# Sherlock considers a string to be valid if all characters of the string
# appear the same number of times. It is also valid if he can remove just
# character at  index in the string, and the remaining characters will occur
# the same number of times. Given a string , determine if it is valid. If so,
# return YES, otherwise return NO.
#
# For example, if , it is a valid string because frequencies are . So is
# because we can remove one  and have  of each character in the remaining
# string. If  however, the string is not valid as we can only remove
# occurrence of . That would leave character frequencies of .
# FIXME: Problem description


def is_valid(s):
    from collections import defaultdict
    c_c = defaultdict(int)

    # Get the character frequencies
    for c in s:
        c_c[c] += 1
    # Get the frequency values and sort them
    f_vals = sorted(c_c.values())

    # If all frequencies are the same then return yes
    if (len(set(f_vals))) == 1:
        return "YES"

    # If the smallest frequency is 1, check of all except the first element
    # is the same, if yes then return YES.
    if f_vals[0] == 1 and len(set(f_vals[1:])) == 1:
        return "YES"

    # Check the largest frequency, if this -1 is the same as other frequencies
    # return yes
    f_vals[len(f_vals) - 1] = f_vals[len(f_vals) - 1] - 1
    if (len(set(f_vals))) == 1:
        return "YES"

    return "NO"


if __name__ == '__main__':
    print(is_valid("aabbbdc"))
    print(is_valid("abcdefghhgfedecba"))
    print(is_valid("aabbccddeefghi"))
