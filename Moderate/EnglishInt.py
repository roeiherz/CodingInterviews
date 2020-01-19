__author__ = 'roeiherz'

"""
Given any int, print an english phrase that describes the int (e.g., "One thousand, two hundred thirty four)
"""

SMALLS = ['Zero', 'One', "Two", 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
          'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
TENS = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
BIGS = ['', 'Thousand', 'Million', 'Billion']


def convert_chunk(x):
    strr = ''
    if x >= 100:
        strr += SMALLS[x/100] + " Hundred"
        x %= 100

    if 10 <= x <= 19:
        strr += ' ' + SMALLS[x]
    elif x > 20:
        strr += ' ' + TENS[x/10]
        x %= 10

    if 1 <= x <= 9:
        strr += ' ' + SMALLS[x]
    return strr


def english_int(x):
    if x == 0:
        return SMALLS[0]
    elif x < 0:
        return "Negative " + english_int(-1 * x)

    chunk_count = 0
    strr = ''
    while x > 0:
        if x % 1000 != 0:
            strr += convert_chunk(x % 1000) + " " + BIGS[chunk_count]

        chunk_count += 1
        x /= 1000

    print(strr.replace('  ', ' '))


if __name__ == '__main__':
    x = 550560
    english_int(x)
