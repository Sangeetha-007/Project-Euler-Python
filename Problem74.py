import math
import time


def next(number):
    number = str(number)
    next_number = 0
    for i in number:
        next_number += math.factorial(int(i))
    return next_number


length = [0]*3000000
chain = []
chain_length = 0
num_chains = 0
for i in range(999999, 1, -1):
    num = i
    while num not in chain:
        if length[num] != 0:
            chain_length = len(chain) + length[num]
            break
        chain.append(num)
        chain_length += 1
        num = next(num)
    for index, n in enumerate(chain):
        length[n] = chain_length - index

    if chain_length == 60:
        num_chains += 1
    chain = []
    chain_length = 0

print('there are', num_chains, 'chains that start below one-million with exactly 60 non-repeating terms
