#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025

#Hence the difference between the sum of the squares of the first ten natural 
#numbers and the square of the sum is 3025 - 385 = 2640.

#Find the difference between the sum of the squares of the 
#first one hundred natural numbers and the square of the sum.

def findSquareDiff(n):
	sumofSquares =0
	sumofNum = (n*(n+1))/2
	i=1
	while i <= n:
		sumofSquares+= i*i
		i+=1
	squareOfSums = sumofNum*sumofNum
	return int(squareOfSums - sumofSquares)
