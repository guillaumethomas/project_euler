from functools import reduce
from prime import is_prime, prime_factor

def mult_3_5():
# euler pb 1
    res = []
    for i in range(3, 1000):
        if i % 3 == 0:
            res.append(i)
        elif i % 5 == 0:
            res.append(i)
    return sum(res)


def fibonnaci(n):
    '''
    Generate the nth item of the Fibonnaci serie
    Fibonnaci serie has n1 = 0 and n2 = 1 with
    s(n) = s(n - 2) - s(n - 1)
    '''
    return sum_series(n)


def sum_series(n, n_1=1, n_2=2):
    '''
    Generate the nth value of a serie of the type s(n) = s(n - 2) + s(n - 1)
    with n1 and n2 known. By default n1 = 0 and n2 = 2, the first 2 values of
    the Fibonnaci serie
    '''
    if n == 1:
        n_elem = n_1
    elif n == 2:
        n_elem = n_2
    else:
        n_elem = sum_series(n - 2, n_1, n_2) + sum_series(n - 1, n_1, n_2)

    return n_elem


def pb_2():
    n = 1
    bool = True
    res = 0
    while bool:
        val = fibonnaci(n)
        if val > 4000000:
            bool = False
        if val % 2 == 0:
            res += val
        if n < 11:
            print(val)
        n += 1

    return res


def pb_4():
    n = 999 * 999
    res = []
    while n >= 100 * 100:
        a = [str(n) == str(n)[::-1], is_prime(n) is False]
        if all(a):
            res.append([n, prime_factor(n)])
        n -= 1
        if len(res) == 20:
            n = 1
    return res


def pb_4_b():
    res = []
    
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            n = i * j
            if str(n) == str(n)[::-1]:
                res.append([n, i, j])
    res.sort(key=lambda x: -x[0])
    return res[0]


def pb_5():
    div = list(range(3, 21))
    div = [3, 6, 7, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 20]
    
    def test(n):
        test = [n % i == 0 for i in div]
        return all(test)

    n = 2520
    while True:
        if test(n) is True:
            break
        if n % 1000 == 0:
            print(n)
        n += 2
    return n


def pb_8():

    with open("./pb_8.txt", 'r') as f:
        a = f.read()
    b = [int(i) for i in list(a) if i != '\n']

    maxi = 0
    for i, j in enumerate(b):
        c = b[i:i + 13]
        d = reduce(lambda x, y: x * y, c)
        if d > maxi:
            maxi = d
            res = c
        if j == len(b) - 13:
            break
    return maxi, res, len(res)


def pb_9():

    def test(i, j, k):
        a = [i**2 + j**2 == k**2, i + j + k == 1000]
        return all(a)

    res = ""
    for i in range(1, 800):
        for j in range(i + 1, 800):
            for k in range(j + 1, 800):
                if test(i, j, k) is True:
                    res = i, j, k, i * j * k
                    break
            if res != "":
                break
        if res != "":
                break
    return res


if __name__ == "__main__":
    a = pb_9()
    print(a)