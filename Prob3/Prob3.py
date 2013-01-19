#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math

def isFactor(n,fact):
        if n % fact ==0:
                return True
                        
#Generate all primes up to n
def generateSieve(num):
        n = int(num)
        sieve = []
        numbers = [0] *n
        i=2
        while i < n :
                #print i, sieve
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

def factorize(n,sieveTable):
        dividers = []
        if sieveTable != None:
                primes = sieveTable
        else:
                primes = generateSieve(math.sqrt(n))
        factored = n
        i=0
        while (i < len(primes) )& (i < n):
                if factored % primes[i] ==0:
                        factored /= primes[i]
                        dividers.append(primes[i])
                        continue
                i +=1
        if factored != 1:
                dividers.append(int(factored))
        return dividers 

        
        
        
        
