# Lilah has a string, , of lowercase English letters that she repeated
# infinitely many times.
#
# Given an integer, , find and print the number of letter a's in the first
# letters of Lilah's infinite string.
#
# For example, if the string  and , the substring we consider is , the first
# characters of her infinite string. There are  occurrences of a in the
# substring.
from helpers import print_output


@print_output
def repeated_string(s: str, n: int):
    # Total a characters count.
    total_a = 0
    # Number of 'a' in the sequence.
    num_a_in_seq = sum([1 for x in s if x == 'a'])
    # Number of times the sequence will fit inside the give number.
    n_complete_seqs = n // len(s)
    # The remainder left in the n after complete strings are fit into it.
    n_char_left = n % len(s)
    total_a += num_a_in_seq * n_complete_seqs
    if n_char_left > 0:
        total_a += sum([1 for x in s[:n_char_left] if x == 'a'])
    return total_a


if __name__ == '__main__':
    repeated_string("aba", 10)
    repeated_string("a", 100)
