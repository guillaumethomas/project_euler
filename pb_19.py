from datetime import datetime, timedelta
from math import factorial

def pb_19():
    sundays = 0
    date = datetime(1901, 1, 1)
    while date != datetime(2001, 1, 1):
        a = [date.day == 1, date.weekday() == 6]
        if all(a):
            sundays += 1
            print('{} {} {}'.format(date, date.weekday(), sundays))
        date += timedelta(days=1)
    return sundays


def pb_20(n):
    return sum([int(i) for i in list(str(factorial(n)))])

if __name__ == "__main__":
    print(pb_19())
    print(pb_20(100))
