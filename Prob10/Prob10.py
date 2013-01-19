#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

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

def sumPrimesBelow(n):
    # Sum all primes below n
    primes = generateSieve(n-1)
    return sum(primes)

