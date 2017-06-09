import math

def result():
    n = 600851475143
    lim = int(math.sqrt(n)) + 1

    for i in range(2, lim):
        while n % i == 0:
            n //= i
            print(i, n)
            if n == 1 or n == i:
                return i

print(result())
