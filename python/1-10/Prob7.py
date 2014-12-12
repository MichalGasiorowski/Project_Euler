#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#we can see that the 6th prime is 13.

#What is the 10 001st prime number?

def findNthPrime(n):
    primes = [2,3]
    k=1
    while True:
        cand1 = 6*k -1
        ok = True
        for prime in primes:
            if cand1 % prime == 0:
                ok= False
                break
        if ok:
            primes.append(cand1)
        if len(primes) == n:
            break
        cand1 = 6*k +1
        ok = True
        for prime in primes:
            if cand1 % prime == 0:
                ok= False
                break
        if ok:
            primes.append(cand1)
        if len(primes) == n:
            break
        k +=1
    return primes[-1]
