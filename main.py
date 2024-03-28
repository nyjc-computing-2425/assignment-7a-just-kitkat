# Write a function to convert numbers to text numerals

OLD_NUM_WORD = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}
# Invert dict
keys = sorted(list(OLD_NUM_WORD.keys()), reverse=True)
NUM_WORD = {}
for i in keys:
    NUM_WORD[i] = OLD_NUM_WORD[i]


def text_numeral(num):
    """
    Converts a number to its word form

    Argument:
    num: int

    Return:
    string -- num in words
    """
    n = num
    num = str(num)
    ans = []
    for word_num in NUM_WORD:
        count = n // word_num
        n -= count * word_num
        if count > 0:
            ans.append(NUM_WORD[word_num])

    return " ".join(ans)
