#!/usr/bin/python

if __name__ == '__main__':
    multiples_of_3_or_5 = [i for i in range(1,1000) if (i % 3 == 0 or i % 5 == 0)]
    sum = 0
    for i in multiples_of_3_or_5:
        sum+=i
    print sum