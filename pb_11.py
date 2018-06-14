from functools import reduce
from numpy import array
from prime import dict_prime
import time


def create_mat():
    with open("pb_11.txt", 'r') as f:
        res = []
        for line in f:
            a = [int(i) for i in list((line.strip('\n')).split(" "))]
            res.append(a)
        return res


def pb_11(mat):

    def horizontal(mat):
        maxi = 0
        k = 15
        for i in mat:
            #k = len(i) - 3
            for j in range(k):
                b = mult(i[j:j + 4])
                if b > maxi:
                    maxi = b
        return maxi

    def diag(mat):
        j = len(mat) - 3
       
        maxi = 0
        for i in range(j):
            for l in range(j):
                a = []
                for k in range(0, 4):
                    a.append(mat[i + k][l + k])
                b = mult(a)
            if b > maxi:
                maxi = b

        return maxi

    def mult(lst):
        return reduce(lambda x, y: x * y, lst)

    diago = diag(mat)
    c = [i[::-1] for i in mat]
    print(c)
    diago_2 = diag(c)
    hor = horizontal(mat)
    mat_t = (array(mat).transpose()).tolist()
    ver = horizontal(mat_t)
    res = [diago, diago_2, hor, ver]

    return max(res)


def tri_n(n):
    return int(n * (n + 1) / 2) 


def nb_divisor(n):
    # https://www.wikihow.com/Determine-the-Number-of-Divisors-of-an-Integer
    dic = dict_prime(n)
    lst = [value + 1 for value in dic.values()]
    return reduce(lambda x, y: x * y, lst)


def tri_div():

    n = 500
    while True:
        m = tri_n(n)
        div = nb_divisor(m)
        if div > 500:
            res = div
            break
        n += 1
        if n % 1000 == 0:
            print('n value {} tri number {} nb divisor {}'.format(n, m, div))
    return m, n, res


def test_divisor(n):
    for i in range(1, n + 1):
        j = tri_n(i)
        print('{} {}'.format(j, nb_divisor(j)))


if __name__ == "__main__":
    start = time.time()
    print(tri_div())
    elapsed = time.time() - start
    print(elapsed)
    
    
