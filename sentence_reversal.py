# Given a string of words, return a string where the order of words is
# reversed of that of the original string.
# Example:
#   "This is the best"
# output:
#   "best the is this"
# Returned sentence can be all lower case.


def reversed_sentence_with_python_tricks(string: str):
    """
    Uses some inbuilt methods in python to reverse.
    Not really the point.
    :param string:
    :return:
    """
    return " ".join(reversed(string.split(" "))).lower()


def reversed_sentence_with_stack(string: str):
    """
    Uses a stack to reverse the string.
    :param string:
    :return:
    """
    words = string.split(" ")
    reversed_words = []
    while len(words) != 0:
        reversed_words.append(words.pop())
    return " ".join(reversed_words).lower()


if __name__ == '__main__':
    print(reversed_sentence_with_python_tricks("This is a string"))
    print(reversed_sentence_with_stack("This is a string"))
