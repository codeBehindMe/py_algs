# Complete the diagonalDifference function below.
def diagonal_difference(arr):
    ldiag = 0
    rdiag = 0
    for i in range(len(arr)):
        ldiag += arr[i][i]
        rdiag += arr[(len(arr) - 1) - i][i]
    return abs(ldiag - rdiag)


if __name__ == '__main__':
    n = 3
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result = diagonal_difference(arr)

    print(str(result) + '\n')
