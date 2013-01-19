##Surprisingly there are only three numbers that can be written as the
##sum of fourth powers of their digits:
##
##    1634 = 1^4 + 6^4 + 3^4 + 4^4
##    8208 = 8^4 + 2^4 + 0^4 + 8^4
##    9474 = 9^4 + 4^4 + 7^4 + 4^4
##
##As 1 = 1^4 is not a sum it is not included.
##
##The sum of these numbers is 1634 + 8208 + 9474 = 19316.
##
##Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
from time import clock
import math



def getSumOfDigit5Power(n,power,digitHash):
    ret = 0
    for digit in str(n):
        ret += digitHash[int(digit)]
    return ret

def findAllPowaNums(power):
    digitHash = {}
    for dig in range(0,10):
        digitHash[dig] = dig**power
    magicNumbers = []
    #find limit tocheck
    limitN =2
    max9 = 9**power
    while True:
        if 10**limitN > limitN * max9:
            break
        limitN +=1
    print(limitN)
    for i in range(2,10**limitN):
        if getSumOfDigit5Power(i,power,digitHash) == i:
            magicNumbers.append(i)
    return magicNumbers,sum(magicNumbers)

start = clock()
print ('5PowaNumbers',findAllPowaNums(5), 'Time:', str(clock() - start)+'s')
