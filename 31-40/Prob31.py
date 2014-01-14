##In England the currency is made up of pound, £,
##and pence, p, and there are eight coins in general circulation:
##
##    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
##
##It is possible to make £2 in the following way:
##
##    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
##
##How many different ways can £2 be made using any number of coins?
from time import clock




def available_coins():
    return sorted([1,2,5,10,20,50,100,200], reverse=True)
    #return sorted([1,2,5], reverse=True)

def goal_sum():
    return 200

def calculate_ways_to_get(av_coins, goal, current_tuple, overall_solution):
    """av_coins sorted descending"""
    if (goal == 0):
        overall_solution.add(current_tuple)
        return
    if(goal < 0 or len(av_coins) == 0):
        return
    calculate_ways_to_get(av_coins, goal - av_coins[0], current_tuple + (av_coins[0],), overall_solution)
    calculate_ways_to_get(av_coins[1:], goal, current_tuple, overall_solution)
    
    

def main():
    start = clock()
    coins = available_coins()
    over_sol = set()
    goal = goal_sum()
    calculate_ways_to_get(coins, goal, (), over_sol)
    #print ("All solutions: " , sorted(over_sol, reverse=True))
    print ("\nNumber of solutions: " , len(over_sol))
    print ('calculate_ways_to_get clocked at', 'Time: ', str(clock() - start)+'s')
    None

if __name__ == "__main__":
    main()
