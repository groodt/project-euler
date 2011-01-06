#!/usr/bin/python
import math
import sys

#tidy generator function. not mine.
def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

#messy sieve of eratosthenes. Mine.
def eratosthenes_primes(n):
    numbers = [i for i in range(2,n)]
    stop = math.ceil(math.sqrt(n))
    i=0
    while numbers[i] < stop:
        prime = numbers[i]
        #print prime
        rest = numbers[i+1:]
        for j in rest:
            if j % prime == 0:
                #print 'not prime: %s' % j
                numbers.remove(j)
        i+=1
    #print len(numbers)
    return numbers
    

if __name__ == '__main__':
    n = 600851475143
    primes = gen_primes()
    prime_factors=[]
    while n > 1:
        factor = primes.next()
        if n % factor == 0:
            #print factor
            prime_factors.append(factor)
            n = n / factor
            
    for p in prime_factors:
        print p
        
    print 'solution: %d' % prime_factors[-1]
        