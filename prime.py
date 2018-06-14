from math import sqrt
from functools import reduce
from collections import defaultdict


def prime_factor(numb):
    n = numb
    lst = []

    while n % 2 == 0:
        n = n / 2
        lst.append(2)

    boolean = True
    k = int(sqrt(n)) + 1
    f = 3
    while boolean:
        if n % f == 0:
            lst.append(f)
            n = n / f
            k = int(sqrt(n)) + 1
            f = 3

        f += 2
        if f > k:
            boolean = False

    if lst != []:
        res = reduce(lambda x, y: x * y, lst)
        if res != numb:
            lst.append(int(n))
    else:
        lst.append(int(n))

    return(lst)

# A function to print all prime factors of a given number n
def prime_factor_2(n):
    res = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        res.append(2)
        n = n / 2
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(sqrt(n)) + 1, 2):
        # while i divides n , print i ad divide n
        while n % i == 0:
            res.append(i)
            n = n / i
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        res.append(n)

    return res



def display_prime(numb):
    lst = prime_factor(numb)
    if len(lst) > 1:
        lst_str = [str(i) for i in lst]
        factors = ', '.join(lst_str)
        str_l = '{} has the following prime factors {}'.format(numb, factors)
    else:
        str_l = '{} is prime'.format(numb)
    return str_l


def is_prime(numb):
    return len(prime_factor(numb)) == 1


def list_prime(n):
    res = [2]
    i = 3
    while True:
        if is_prime(i):
            res.append(i)
        if len(res) == n:
            break
        i += 2
    return res


def dict_prime(n):
    lst = prime_factor_2(n)
    res = defaultdict(int)
    for i in lst:
        res[i] += 1
    return dict(res)


def list_prime_inf(n):
    res = [2]
    i = 3
    summ = res[0]
    while True:
        if is_prime(i):
            if i > n:
                break
            res.append(i)
            summ += i
        i += 2
    return res, summ


if __name__ == "__main__":
    '''
    'print(prime_factor(8))
    'print(prime_factor(9))
    'print(prime_factor(163))
    'print(prime_factor(164))
    '''
    a, b = list_prime_inf(2000000)
    print(a)
    print(b)
