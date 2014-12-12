#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2

#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#c <= 500
import math
from operator import mul
from functools import reduce
def checkIfPythagorean(a,b,c):
    return a*a + b*b == c*c
def findTriplet(n):
    #Find (a,b,c) Triplet that a+b+c=1000 a^2+b^2=c^2
    triplet = (0,0,0)
    c=math.ceil(n/2)
    lowerBound = math.ceil(n/3)
    b=c -1
    a = 1
    found = False
    #print ('lowerBound:',lowerBound)
    while c > lowerBound:
        b = c -1
        while b > math.ceil((n-c)/2):
            a = n - c -b
            if checkIfPythagorean(a,b,c):
                triplet = (a,b,c)
                return triplet, reduce(mul,triplet)
            b -= 1
        c-=1
    return triplet,0

def getTripletList(maxN):
    ret = []
    for i in range(1,maxN+1):
        triplet = findTriplet(i)
        if triplet[1] == 0:
            continue
        ret.append([i,triplet])
    return ret
