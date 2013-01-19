#A perfect number is a number for which the sum of its proper divisors 
#is exactly equal to the number. For example, the sum of the proper divisors 
#of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less 
#than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
#the smallest number that can be written as the sum of two abundant numbers is 24. 
#By mathematical analysis, it can be shown that all integers greater than 28123 can 
#be written as the sum of two abundant numbers. However, this upper limit cannot be reduced 
#any further by analysis even though it is known that the greatest number that cannot be 
#expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

#################
#To get the sum of divisors consider the following: if n = 220 say, then n = 2^2 * 5^1 * 11^1
#and the sum of its divisors is given by
# d(n) = (2^3-1)   (5^2-1)   (11^2-1)
#        ------- * ------- * -------- = 284
#           1        4          10
# and this can be generalized once we know the prime factors of the number.
################

# 1. Get List of Abundant Numbers < 28123
# 2. Sort the list ascending
# 3. Find Numbers which cannot be sum of 2 ABNUms
# 4. Sum Them

import itertools
import math
from operator import mul
from functools import reduce
from time import clock

def generateSieve(num):
    n = int(num)
    sieve = []
    numbers = [0] *n
    i=2
    while i < n :
        if numbers[i] == 1:
            i += 1
            continue
        if numbers[i] ==0: # This is a prime number
            sieve.append(i)
        if 2*i >= n:
            i +=1
            continue
        j=i
        while True:
            j += i
            if j >= n:
                break
            numbers[j] = 1
        i += 1
    return sieve

def factorize(n,sieveTable=None):
    if n <=1:
        return [1]
    dividers = [1]
    if sieveTable != None:
        primes = sieveTable
    else:
        primes = generateSieve(max(math.sqrt(n),100))
    factored = n
    i=0
    lenght = len(primes)
    lqr = int(math.sqrt(n))
    while (i < lenght )& (i < lqr):
        if factored == 1:
            break
        if factored % primes[i] ==0:
            factored /= primes[i]
            dividers.append(primes[i])
            continue
        i +=1
    if factored != 1:
        dividers.append(int(factored))
    if dividers[-1] == n:
        dividers.remove(n)
    return dividers

def getSumOfDivisors(n,sieveTable=None):
    dividers = factorize(n,sieveTable)
    dividers.remove(1)
    #print (dividers)
    primeFactors = set(dividers)
    ret = 1
    for prime in primeFactors:
        occurs = dividers.count(prime)
        coff = (prime**(occurs+1) -1)/(prime - 1)
        #print (prime, occurs, coff)
        ret *= coff
    return int(ret/2)
	
def isAbundantNumber(n,sieveTable=None):
    if getSumOfDivisors(n,sieveTable) > n :
        return True
    return False

def findNearestSmallerAbNum(n, abTable):
    lenght = len(abTable)
    if abTable[-1] < n:
        return lenght -1
    foundInd = 0

def sumOfImpossibleAbNum(n=28123):
    maxAb = min(28123,n)
    sieve = generateSieve(maxAb)
    tableOfAb = []
    i =1
    k=1
    abSet = set([])
    while i <= maxAb:
        if isAbundantNumber(i,sieve):
            tableOfAb.append(i)
            abSet.add(i)
        #if i % 500 == 0:
        #    print (i)
        i+=1
    numToCheck=1
    lenghtAb = len(tableOfAb)
    impossAb = []
    while numToCheck <= maxAb:
        abTableIndex=0
        while (abTableIndex < lenghtAb):
            diff = numToCheck - tableOfAb[abTableIndex]
            #print (numToCheck, tableOfAb[abTableIndex],diff)
            if diff < 0:#Hooray!
                impossAb.append(numToCheck)
                break
            if diff in abSet:
                abTableIndex+=1
                break
            abTableIndex+=1
        numToCheck+=1
    return sum(impossAb)

start = clock()
print (sumOfImpossibleAbNum(), clock() - start,'seconds')






