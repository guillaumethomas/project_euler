

def pb_13():
    with open('pb_13.txt', 'r') as f:
        res = []
        summ = 0
        for line in f:
            a = int(line.strip('\n'))
            res.append(a)
            summ += a
    return str(a)[:10], res


if __name__ == "__main__":
    summi, res = pb_13()
    print(summi)
