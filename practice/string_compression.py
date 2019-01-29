# Given a string in the form AAAABBCCC compress the string to become
# A4B2C3.
# Falsely compressing strings eg B1 is allowed.


def compress_string(string: str):
    """
    Compresses a string.
    :param string:
    :return:
    """
    if len(string) == 0:
        return ""
    if len(string) == 1:
        return string + "1"

    cur_char = string[0]
    cur_char_num = 1
    output = [] + [cur_char]
    for c in string[1:]:
        if c == cur_char:
            cur_char_num += 1
        else:
            output.append(str(cur_char_num))
            output.append(c)
            cur_char = c
            cur_char_num = 1
    output.append(str(cur_char_num))
    return "".join(output)


def compress_string_safe(string: str):
    """
    Compresses a string but handles where the single letters are there.
    :param string:
    :return:
    """
    cur_char = string[0]
    cur_char_num = 1
    output = []
    for c in string[1:]:
        if c == cur_char:
            cur_char_num += 1
        else:
            output.append(cur_char)
            if cur_char_num > 1:
                output.append(str(cur_char_num))
            cur_char_num = 1
            cur_char = c
    output.append(cur_char)
    if cur_char_num > 1:
        output.append(str(cur_char_num))
    return "".join(output)


if __name__ == '__main__':
    print(compress_string("AAABBCCCC"))
    print(compress_string_safe("AAABBCCCC"))
    print(compress_string("ABBCCCC"))
    print(compress_string_safe("ABBCC"))
