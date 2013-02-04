#A permutation is an ordered arrangement of objects.
#For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
#If all of the permutations are listed numerically or alphabetically,
#we call it lexicographic order. The lexicographic permutations of
#0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits
#0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math
from time import clock

def getLexiOrder(n,ord_ind):
    if math.factorial(n) < ord_ind:
        return None
    listOfNum = list(range(0,n))
    curr_fac = n - 1 
    ord_left = ord_ind 
    rest = 0
    toRet =''
    while curr_fac >=0:
        rest,ord_left = divmod(ord_left,math.factorial(curr_fac))
        toIns = listOfNum[rest]
        toRet += str(toIns)
        listOfNum.remove(toIns)
        curr_fac -=1
    return toRet

start = clock()
print ('LexiOrder:',getLexiOrder(10,10**6 -1),'Time:', str(clock() - start)+'s')

if __name__ == "__main__": # local
    import doctest
    doctest.testmod(report=True,verbose=True,exclude_empty=True)
elif __name__ == "main":   # web interpreter (Udacity)
    import doctest, main
    doctest.testmod(main,report=True,verbose=True,exclude_empty=True)
