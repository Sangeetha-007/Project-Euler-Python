import math

f = open('base_exp.txt', 'r')
base_exponents = f.read()
base_exp = [ b_e for b_e in base_exponents.split('\n')] # put all base-exponents in lis

line_index = 0
max_value = 0

for index, line in enumerate(base_exp): # go through list of base-exponents
    t = tuple([int(x) for x in line.split(',')])  # put each base-exponent pair in tuple
    value = t[1]*math.log(t[0], 10)  # multiple exponent with log base 10 of base
    if value > max_value:
        max_value = value
        line_index = index

print('largest value in line#', line_index + 1)
