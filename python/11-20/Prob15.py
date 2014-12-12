#Starting in the top left corner of a 2×2 grid, 
#there are 6 routes (without backtracking) to the bottom right corner.

# --- --. --.
# ..| .|- .|.
# ..| ..| .|-
#
# -.. |.. |..
# |-- |-. |..
# ..| .|- |..
#How many routes are there through a 20×20 grid?

def howManyPaths(xx,yy):
    x = xx+1
    y = yy+1
    i=x-2
    j=y-2
    #grid = [[0]*(y-1) + [1] ]*(x-1) + [[1]*y]
    #grid = [[0]* y]*x    # Haha very funny, doesnt work!
    grid = [[0]*y for n in range(x)]
    k=0
    kk =0
    print (grid)
    while k < x:
        kk = 0
        while kk < y:
            if (k == x-1 ) | (kk == y-1):
                grid[k][kk] = 1
            kk+=1
        k+=1
    grid[x-1][y-1] = 0
    while i >=0:
        j=x-2
        while j >=0:
                #print ('-----------\n','i:', i, 'j:', j ,' XX',grid)
                grid[i][j] = grid[i][j+1] + grid[i+1][j]
                #print ('i:', i, 'j:', j ,' XX',grid)
                j-=1
        i-=1
    return grid
