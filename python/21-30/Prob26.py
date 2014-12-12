##A unit fraction contains 1 in the numerator. The decimal representation of
##the unit fractions with denominators 2 to 10 are given:
##
##    1/2	= 	0.5
##    1/3	= 	0.(3)
##    1/4	= 	0.25
##    1/5	= 	0.2
##    1/6	= 	0.1(6)
##    1/7	= 	0.(142857)
##    1/8	= 	0.125
##    1/9	= 	0.(1)
##    1/10	= 	0.1
##
##Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
##It can be seen that 1/7 has a 6-digit recurring cycle.
##
##Find the value of d < 1000 for which 1/d contains the longest
##recurring cycle in its decimal fraction part.

from time import clock

def findCycleOFFraction(a,b):
    aNorm = a % b
    cycle=0
    divDict = {}
    newDigit =aNorm
    retFrac = str(divmod(a,b)[0]) + '.'
    pos = 1
    while True:
        #print (divPair,10*divPair[0],b)
        divPair = divmod(10*newDigit,b)
        newDigit = divPair[1]
        #print (divPair)
        if divPair in divDict: # Found Cycle
            cycle = pos - divDict[divPair]
            break
        divDict[divPair] = pos
        retFrac +=str(divPair[0])
        pos+=1
    return cycle, retFrac

def findDWithMaxCycle(n):
    maxCycle =0
    maxD = 0
    maxFraction =''
    d= n-1
    while d > 2:
        if d < maxCycle:
            break
        cycle,tempFraction = findCycleOFFraction(1,d)
        #print (d,cycle,tempFraction)
        if cycle > maxCycle:
            maxCycle = cycle
            maxD = d
            maxFraction = tempFraction
        d-=1
    return maxD,maxCycle,maxFraction

start = clock()
print ('Best:',findDWithMaxCycle(1000)[:-1], 'Time:', str(clock() - start)+'s')



