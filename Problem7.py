# 10 001st prime number

first19 = {
    0: '',
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

tens = {
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
}

hundreds = {
    100: 'onehundred', 200: 'twohundred', 300: 'threehundred', 400: 'fourhundred', 500: 'fivehundred',
    600: 'sixhundred', 700: 'sevenhundred', 800: 'eighthundred', 900: 'ninehundred'
}

string = ''  # start with empty string
for i in range(1, 1000):
    if i in first19.keys():
        string += first19[i]
    elif i < 100:  # from 20 to 99
        string = string + tens[int(i - i % 10)] + first19[i % 10]
    else:  # from 100 to 999
        if i % 100 in first19.keys():  # if last 2 digits are in first19 keys
            string = string + hundreds[i - i % 100] + ('and' if i % 100 > 0 else '') + first19[i % 100]
        else:
            string = string + hundreds[i - i % 100] + 'and' + tens[int((i % 100)//10) * 10] + first19[i % 10]

string += 'onethousand'  # add one thousand to the string
print('one to one-thousand written out takes', len(string), 'characters')
