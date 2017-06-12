import itertools

# takes about 10 - 20 seconds to run, depending on your machine


sum_pans = 0
numb = '1234567890'
for pan in itertools.permutations(numb):  # gives all permutations of numb

    next_num = ''.join(pan)  # convert tuple to string
    if int(next_num[1:4]) % 2 == 0 and int(next_num[2: 5]) % 3 == 0 and int(next_num[3: 6]) % 5 == 0 \
            and int(next_num[4: 7]) % 7 == 0 and int(next_num[5: 8]) % 11 == 0 and int(next_num[6: 9]) % 13 == 0 \
            and int(next_num[7: 10]) % 17 == 0:
        sum_pans += int(next_num) # add to sum after converting to int

print(sum_pans)
