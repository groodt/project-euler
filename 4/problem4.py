#!/usr/bin/python

def inner(i):
    j=999
    while j > 1:
        number = i * j
        #print number
        forward_str = str(number)
        backwards_str = forward_str[::-1]
        #print backwards_str
        if forward_str == backwards_str:
            return number    
        j-=1
    return -1

if __name__ == '__main__':
    i = 999
    palindromes=[]
    while i > 1:
        result = inner(i)
        if result != -1:
            palindromes.append(result)
        i-=1
    palindromes.sort()
    for i in palindromes:
        print i
     

            
        