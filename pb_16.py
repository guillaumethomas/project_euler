from num2words import num2words


def pb_16():
    a = 2**1000
    b = [int(i) for i in list(str(a))]
    c = sum(b)
    return c


def pb_17():

    a = list(range(1, 1001))
    b = [num2words(i) for i in a]
    c = [(i.replace(' ', '')).replace('-', '') for i in b]
    print(c[-1])
    d = [len(i) for i in c]
    return sum(d)


if __name__ == "__main__":
    print(pb_17())
