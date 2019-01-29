# Computing the hourglass sum
from helpers import print_output


@print_output
def hourglass_sum(arr):
    # Define the hourglass
    hourglass = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    sums = []

    def elem_mul(arr1, arr2):
        """
        Elementwise multiplication of two 2d arrays.
        :param arr1:
        :param arr2:
        :return:
        """
        return [[a * b for a, b in zip(i, j)] for i, j in zip(arr1, arr2)]

    def subset_elements(arr, start_row, end_row, start_col, end_col):
        rows = arr[start_row:end_row]
        for r in rows:
            yield r[start_col:end_col]

    def nested_sum(nested_list):
        return sum([item for sublist in nested_list for item in sublist])

    # Scan over the matrix indices and elementwise sum
    for i in range(4):
        for j in range(4):
            a = list(subset_elements(arr, i, i + 3, j, j + 3))
            e_mul = elem_mul(hourglass, a)
            sums.append(nested_sum(e_mul))
    return max(sums)


if __name__ == '__main__':
    m1 = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3],
          [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]
    m2 = [[0, -4, -6, 0, -7, -6, ], [-1, -2, -6, -8, -3, -1],
          [-8, -4, -2, -8, -8, -6], [-3, -1, -2, -5, -7, -4],
          [-3, -5, -3, -6, -6, -6], [-3, -6, 0, -8, -6, -7]]
    m3 = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],
          [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    hourglass_sum(m3)
