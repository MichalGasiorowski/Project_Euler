##Consider all integer combinations of a^b for 2 <= a <= 5 and 2 <= b <= 5:
##
##    2^2=4, 2^3=8, 2^4=16, 2^5=32
##    3^2=9, 3^3=27, 3^4=81, 3^5=243
##    4^2=16, 4^3=64, 4^4=256, 4^5=1024
##    5^2=25, 5^3=125, 5^4=625, 5^5=3125
##
##If they are then placed in numerical order, with any repeats removed,
##we get the following sequence of 15 distinct terms:
##
##4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
##
##How many distinct terms are in the sequence generated
##by a^b for 2 <= a <= 100 and 2 <= b <= 100?
##-----------------------------------------------------------------------

from time import clock
from math import sqrt
def findAllIntComb(a,b):
    setOfComb = set([])
    cou = 0
    for ai in range(2,a+1):
        for bi in range(2,b+1):
            ax,bx=ai,bi
            while True:
                if ( (sqrt(ax) <2 ) | (bx*2 >b) | ( (int(sqrt(ax))) **2 !=ax )) :
                    break
                ax = sqrt(ax)
                bx = bx*2
            #print((ax,bx))    
            if (ax,bx) in setOfComb:
                cou+=1
                #print ((ai,bi) , "is",(int(ax),bx), "Whoho!" )
            else:
                setOfComb.add((int(ax),int(bx)))
    return sorted(list(setOfComb)),len(setOfComb),cou, (a -1)**2-cou
def findAllIntCombBrute(a,b):
    setOfComb = set([])
    for ai in range(2,a+1):
        for bi in range(2,b+1):
            setOfComb.add(ai**bi)
    return setOfComb

start = clock()
res = findAllIntCombBrute(100,100)
print ('Count',len(res), 'Time:', str(clock() - start)+'s')
