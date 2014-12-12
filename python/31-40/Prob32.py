##We shall say that an n-digit number is pandigital if it
##makes use of all the digits 1 to n exactly once; for example,
##the 5-digit number, 15234, is 1 through 5 pandigital.
##
##The product 7254 is unusual, as the identity, 39 × 186 = 7254,
##containing multiplicand, multiplier, and product is 1 through 9 pandigital.
##
##Find the sum of all products whose multiplicand/multiplier/product
##identity can be written as a 1 through 9 pandigital.
##HINT: Some products can be obtained in more than one way
##so be sure to only include it once in your sum.
from time import clock
import math
from functools import lru_cache

last_digits_impossible = set( ( (1,1), (1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),
                               (2,2), (2,5), (2,6), (3,3), (3,5), (4,4), (4,5), (5,5),
                               (5,6),(5,7), (5,8), (5,9) , (6, 6), (6,8), (7,7),
                               (8,8), (9,9)))

@lru_cache(maxsize=None)
def is_pandigital(num):
    digit_set = set()
    i = num
    while(i >= 1):
        rem = i % 10
        if rem in digit_set:
            return False
        digit_set.add(rem)
        i = int(i / 10)
    return True
        

def main():
    start = clock()
    
    

if __name__ == "__main__":
    main()
