#You are given the following information, but you may prefer to do some research for yourself.

#    1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not 
#on a century unless it is divisible by 400.

#How many Sundays fell on the first of the month during 
#the twentieth century (1 Jan 1901 to 31 Dec 2000)?

months = [31,28,31,30,31,30,31,31,30,31,30,31]
monthsLeap = [31,29,31,30,31,30,31,31,30,31,30,31] 

#0-Sunday,1-Monday,2-Tuesday,3-Wednesday,4-Thursday,5-Friday,6-Saturday

# 

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0 :
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def getNumberOfSundaysOnFirstOfMonth(year,startingDay):
    #1 - Sunday
    ret= 0
    if isLeapYear(year):
        monthsUsed = monthsLeap
    else:
        monthsUsed = months
    #if startingDay ==1:
    #    ret +=1
    tableOfSpecialMonths=[]
    i=0
    startingDayOfMonth = startingDay
    while i < 12:
        #print (i,startingDayOfMonth,monthsUsed[i])
        if startingDayOfMonth ==0:
            tableOfSpecialMonths.append(i)
            ret +=1
        startingDayOfMonth = (startingDayOfMonth + monthsUsed[i] )%7
        i+=1
    return ret,startingDayOfMonth

def getSundaysOn1MonthAll(yearStart,yearStop,dayStart):
    ret = 0
    currYear = yearStart
    nextDay = dayStart
    toAdd = 0
    while currYear <= yearStop :
        toAdd,nextDay = getNumberOfSundaysOnFirstOfMonth(currYear,nextDay)
        ret += toAdd
        #print ('CurrentYear:',currYear,'toAdd:',toAdd,'nextYear1Day:',nextDay)
        currYear +=1
    return ret

