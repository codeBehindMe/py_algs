# Increments an integer sequence.
# Example:
# [3,1,4,1,5,9] + 1
#  [3,1,4,1,6,0]


def incr_int_seq_recur(int_seq: [int]) -> [int]:
    def incr_int_tail_call(int_seq: [int], index: int) -> [int]:
        # If index is less than 0, that means we need to insert a 1
        # to the left of the array.
        if index < 0:
            int_seq.insert(0, 1)
            return int_seq
        # Check if the number in the current index + 1 is greater than 9
        # If so set the value of the current index to 0.
        # Then call increment on the element to the left by one.
        if int_seq[index] + 1 > 9:
            int_seq[index] = 0
            return incr_int_tail_call(int_seq, index - 1)
        # If it doesn't simply increment the value at that index and return.
        int_seq[index] = int_seq[index] + 1
        return int_seq
    return incr_int_tail_call(int_seq, len(int_seq) - 1)


if __name__ == '__main__':
    la = [3, 1, 4, 1, 5, 9]
    lb = [9, 9]
    lc = [9, 9, 9, 1, 9, 9]

    print(incr_int_seq_recur(la))
    print(incr_int_seq_recur(lb))
    print(incr_int_seq_recur(lc))
