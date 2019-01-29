# Given two strings check if they are anagrams of each other.
# The anagrams are character level, meaning whitespace and capitalisation can
# be ignored and characters from different words can be used to form another
# word.
# Examples.
#   "public relations" is an anagram of "crap built on lies"
#   "clint eastwood" is an anagram of "old west action"


def is_anagram(string1, string2):
    """
    Given two strings, check's if they're an anagram of each other.
    Doesn't recognise true words from fake words.
    # Runtime: max(O(n),O(m))
    :param string1:
    :param string2:
    :return:
    """

    # Compose a character level count of the first string.
    # Do this natevely without using itertools.
    def create_char_map(string):
        """
        Full scan O(n)
        :param string:
        :return:
        """
        # Remove whitespace and decapitalise
        string = string.replace(" ", "").lower()
        c_map = {}
        for c in string:
            try:
                c_map[c] += 1
            except KeyError:
                c_map[c] = 1
        return c_map

    str_1_map = create_char_map(string1)
    str_2_map = create_char_map(string2)

    # If equal, they are anagrams.
    if str_1_map == str_2_map:
        return True
    # Else they are not.
    return False


def is_anagram_sorted(string1, string2):
    """
    Uses sorting to see if two strings are anagrams of each other.
    Runtime is worst case O(nLogn)
    :param string1:
    :param string2:
    :return:
    """
    # Do a best case O(n) check
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    if len(string1) != len(string2):
        return False

    if sorted(string1) == sorted(string2):
        return True
    else:
        return False


if __name__ == '__main__':
    string_1 = "public relations"
    anagram_1 = "crap built on lies"

    assert is_anagram('go go go', 'gggooo') == True
    assert is_anagram('abc', 'cba') == True
    assert is_anagram('hi man', 'hi     man') == True
    assert is_anagram('aabbcc', 'aabbc') == False
    assert is_anagram('123', '12') == False

    assert is_anagram_sorted('go go go', 'gggooo') == True
    assert is_anagram_sorted('abc', 'cba') == True
    assert is_anagram_sorted('hi man', 'hi     man') == True
    assert is_anagram_sorted('aabbcc', 'aabbc') == False
    assert is_anagram_sorted('123', '12') == False
