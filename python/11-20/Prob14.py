#The following iterative sequence is defined for the set of positive integers:

#n › n/2 (n is even)
#n › 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:
#13 › 40 › 20 › 10 › 5 › 16 › 8 › 4 › 2 › 1

#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

def GetNextCollatz(n):
        if n %2 ==0:
                return int(n/2)
        return 3 * n +1

def getCollatzNumber(maxN):
        collatzTable = [0] * maxN
        collatzTable[1] =1
        num = 1
        tempTable = []
        nextNum = 0
        retTemp =1
        while num < maxN:
                if collatzTable[num] != 0:# was calculated earlier
                        num +=1
                        continue
                tempTable = [num]
                nextNum = num
                while True:
                        nextNum = GetNextCollatz(nextNum)
                        #print (num,nextNum)
                        if nextNum < maxN:
                                if collatzTable[nextNum] != 0:
                                        retTemp = collatzTable[nextNum]
                                        tempTable.append(nextNum)
                                        break
                        tempTable.append(nextNum)
                i = 0
                #print ('======================================')
                #print ('num:',num,'tempTable:',tempTable, 'retTemp:',retTemp,'CollatzTable:',collatzTable)
                length = len(tempTable)
                while i < length: # for every item in tempTable, going reverse...
                        #print (length,i,tempTable)
                        item = tempTable[length-i-1]
                        #print (i,item)
                        if item < maxN:
                                if item != 1:
                                        collatzTable[item] = retTemp + i 
                        i+=1
                #print('------------------------')
                #print ('num:',num,'tempTable:',tempTable, 'retTemp:',retTemp,'CollatzTable:',collatzTable)
                num+=1
        return collatzTable

def findMaxAndIndex(p):
        ind = 0
        maxItem =0
        maxIndex = 0
        lenOfList = len(p)
        while ind < lenOfList:
                if p[ind] > maxItem:
                        maxIndex = ind
                        maxItem = p[ind]
                ind += 1
        return (maxIndex,maxItem)
                        



