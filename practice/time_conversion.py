def timeConversion(s):
    #
    # Write your code here.
    #
    def decompose_numerals(string):
        return (map(int, string.split(":")))

    ho, mi, se = decompose_numerals(s[:-2])  # Nums
    d = s[-2:]  # The sign

    if ho == 12 and d == "AM":
        return "00:{0:02d}:{1:02d}".format(mi, se)

    if ho == 12 and d == "PM":
        return s[:-2]

    if d == "PM" and ho > 12:
        return "{0:02d}:{1:02d}:{2:02d}".format(ho + 12, mi, se)

    if d == "AM":
        return "{0:02d}:{1:02d}:{2:02d}".format(ho, mi, se)


if __name__ == '__main__':
    print(timeConversion("12:40:22PM"))
