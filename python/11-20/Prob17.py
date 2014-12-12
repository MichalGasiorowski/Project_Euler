#If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
#then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were 
#written out in words, how many letters would be used?

#NOTE: Do not count spaces or hyphens. For example, 
#342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
#contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


numberWordDict = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',
12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
20:'twenty', 30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}                  
numberWordDictCount = {}
for key in numberWordDict.keys():
    numberWordDictCount[key] = len(numberWordDict[key])

def countLettersInNumber(num):
    retSum = 0
    ss = str(num)
    fullName =''
    if num >=1000:
        retSum += (numberWordDictCount[int(ss[0])] + numberWordDictCount[1000])
        fullName += (numberWordDict[int(ss[0])] + numberWordDict[1000])
        if ss[-3:] != '000':
            retSum +=3 #'and'
            fullName += 'and'
    if num >= 100:
        if ss[-3:] != '000':
            retSum += (numberWordDictCount[int(ss[-3])] + numberWordDictCount[100])
            fullName += (numberWordDict[int(ss[-3])] + numberWordDict[100])
        if ss[-2:] != '00':
            retSum += 3 #'and'
            fullName += 'and'
    if num % 100 >=20:
        retSum += ( numberWordDictCount[int(ss[-2])*10] + numberWordDictCount[int(ss[-1])] )
        fullName += ( numberWordDict[int(ss[-2])*10] + numberWordDict[int(ss[-1])] )
    else:
        #print (int(ss[-2:]))
        retSum += ( numberWordDictCount[int(ss[-2:])] )
        fullName += ( numberWordDict[int(ss[-2:])] )
    return retSum,fullName

def countLettersTillN(n):
    # only to 1000
    retSum =0
    temp = 0
    i=0
    names = []
    name = ''
    while i <= n:
        temp, name = countLettersInNumber(i)
        retSum +=temp
        i+=1
        names.append(name)
    return names,retSum


        
