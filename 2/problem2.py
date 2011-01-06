#!/usr/bin/python

def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    even_fib_series = [i for i in fib(4000000) if (i >= 2 and i % 2 == 0)]
    sum = 0;
    for i in even_fib_series:
        sum+=i
    print sum
        