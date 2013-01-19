#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def isNumAPalindrome(n):
	st = str(n)
	k=0
	length = len(st)
	while k <= length/2:
		if st[k] != st[length -k - 1]:
			return False
		k+=1
	return True

def check3DigitsMults():
        n=1000
        ret = 0
        i=1
        j=1
        while i < 200 :
                j=1
                while j < 200:
                        numb = (n-i)*(n-j)
                        #print (i,j,numb)
                        if isNumAPalindrome(numb):
                                print ("YES:",numb, n-i,n-j)
                                ret = max(ret,numb)
                        j+=1
                i+=1
        return ret
