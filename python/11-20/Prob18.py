#By starting at the top of the triangle below and moving to 
#adjacent numbers on the row below, the maximum total from top to bottom is 23.

#   3
#  7 4
# 2 4 6
#8 5 9 3

#That is, 3 + 7 + 4 + 9 = 23.

#Find the maximum total from top to bottom of the triangle below:

#               [[75],
#              [95, 64],
#             [17, 47, 82],
#            [18, 35, 87, 10],
#           [20, 4, 82, 47, 65],
#          [19, 1, 23, 75, 3, 34],
#         [88, 2, 77, 73, 7, 63, 67],
#        [99, 65, 4, 28, 6, 16, 70, 92],
#       [41, 41, 26, 56, 83, 40, 80, 70, 33],
#     [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#   [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#  [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
# [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]],

#NOTE: As there are only 16384 routes, it is possible to 
#solve this problem by trying every route. 
#However, Problem 67, is the same challenge with a triangle containing 
#one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

triangle =                [[75],
              [95, 64],
             [17, 47, 82],
            [18, 35, 87, 10],
           [20, 4, 82, 47, 65],
          [19, 1, 23, 75, 3, 34],
         [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
       [41, 41, 26, 56, 83, 40, 80, 70, 33],
     [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
   [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
  [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
 [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]



class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data

def constructDict(dataList):
    i=0
    length_i = len(dataList)
    #print (length_i)
    triangleDict = {}
    while i < length_i:
        j=0
        length_j = len(dataList[i])
        #print (length_j)
        while j < length_j:
            #print (i,j,length_i,length_j)        #next coordinates #bestSum
            triangleDict[i,j] = [dataList[i][j],[[0,0],0]]
            j+=1
        i+=1
    return triangleDict
def findMaxTraverse(triangleIn):
    triangleDict = constructDict(triangleIn)
    length_i=len(triangleIn)
    i= length_i - 2
    while i >=0:	
        length_j = len(triangleIn[i])
        j= length_j - 1
        while j >= 0:
            if triangleDict[i+1,j][0] + triangleDict[i+1,j][1][1]  > triangleDict[i+1,j+1][0] + triangleDict[i+1,j+1][1][1]:
                triangleDict[i,j][1] = [[i+1,j],triangleDict[i+1,j][0] + triangleDict[i+1,j][1][1]]
            else:
                triangleDict[i,j][1] = [[i+1,j+1],triangleDict[i+1,j+1][0] + triangleDict[i+1,j+1][1][1]]
            j -= 1
        i -= 1
    return triangleDict, triangleDict[0,0][1][1] + triangleDict[0,0][0]

    
