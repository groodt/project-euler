#!/usr/bin/python
import math

def gen_step_counter(n):
    count=n
    while True:
        yield count
        count+=n
        
def evenly_divisible_up_to(n,limit):
    divisors=[i for i in range(1,limit)]
    evenly_divisible=True
    for divisor in divisors:
        if n % divisor == 0:
            continue
        else:
            return False
    return evenly_divisible
        

if __name__ == '__main__':
    n=20
    steps = gen_step_counter(n)
    while True:
        candidate = steps.next()
        #print candidate
        if evenly_divisible_up_to(candidate, n):
            print candidate
            break
    

            
        