#!/usr/bin/python
import math

if __name__ == '__main__':
    n=100
    sum_first_hundred=sum(i for i in range(1,n+1))
    squared_sum_first_hundred=sum_first_hundred*sum_first_hundred
    print squared_sum_first_hundred
    
    sum_first_hundred_squares=sum(i*i for i in range(1,n+1))
    print sum_first_hundred_squares
    
    print 'difference %d' % (squared_sum_first_hundred-sum_first_hundred_squares)
    

            
        