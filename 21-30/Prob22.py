#Using names.txt (right click and 'Save Link/Target As...'), 
#a 46K text file containing over five-thousand first names, begin by sorting 
#it into alphabetical order. Then working out the alphabetical value for each name, multiply 
#this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, 
#which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
#So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?

def getNames():
    f = open('names.txt', 'r')
    st = f.read().split(',')
    st.sort()
    return st

def getWordScore(word):
    # ord('A') = 65
    ret = 0
    for c in word:
        ret += (ord(c) - 65 +1)
    return ret

def getSumOfNameValues():
    names = getNames()
    ret = 0
    i=0
    lenght = len(names)
    while i < lenght:
        value = getWordScore(names[i]) * (i +1)
        #print (i +1, names[i],value)
        ret += value
        i+=1
    return ret
    
    


