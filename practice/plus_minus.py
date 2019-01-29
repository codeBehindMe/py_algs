# Complete the plusMinus function below.
def plusMinus(arr):
    neg_count = 0
    zero_count = 0
    for num in arr:
        if num < 0:
            neg_count += 1
        elif num == 0:
            zero_count += 1

    neg_rat = neg_count / len(arr)
    pos_rat = (len(arr) - (neg_count + zero_count)) / len(arr)
    zero_rat = zero_count / len(arr)

    return neg_rat, pos_rat, zero_rat


if __name__ == '__main__':
    a = [-4, 3, -9, 0, 4, 1]

    print(plusMinus(a))
