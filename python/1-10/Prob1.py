#If we list all the natural numbers below 10 that are multiples 
#of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

# 3 + 6  + 9 + .. 999 = 

def art_sum(a1,n,r):
	return ((2*a1 + (n-1)*r)*n)/2
def howManyMultiplies(n,div):
	ret = int(n/div)
	if n%div == 0 :
		ret -= 1
	return ret
	
def findAllMultBy(n,div1,div2):
	ret = art_sum(div1,howManyMultiplies(n,div1),div1) + \
	art_sum(div2,howManyMultiplies(n,div2),div2) - \
	art_sum(div1 * div2,howManyMultiplies(n,div1*div2),div1*div2)
	return ret
