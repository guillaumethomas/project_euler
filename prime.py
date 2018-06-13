from math import sqrt
from functools import reduce


def prime_factor(numb):
    n = numb
    lst = []

    while n % 2 == 0:
        n = n / 2
        lst.append(2)

    boolean = True
    k = int(sqrt(n))
    f = 3
    while boolean:
        if n % f == 0:
            lst.append(f)
            n = n / f
            k = int(sqrt(n))
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
