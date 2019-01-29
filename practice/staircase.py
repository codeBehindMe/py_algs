import sys


# Complete the staircase function below.
def staircase(n):
    pass
    for i in reversed(range(n)):
        for j in range(n):
            if j >= i:
                sys.stdout.write("#")
            else:
                sys.stdout.write(" ")
        sys.stdout.write("\n")


if __name__ == '__main__':
    n = 5

    staircase(n)
