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
from functools import lru_cache

sol_count = 0

def available_coins():
    return tuple(sorted([1,2,5,10,20,50,100,200]))


def goal_sum():
    return 200

def calculate_ways_to_get(av_coins, goal, current_solution, overall_set):
    """av_coins sorted descending"""
    global sol_count
    if (goal == 0):
        overall_set.add(current_solution)
        sol_count += 1
        return
    if(goal < 0 or len(av_coins) == 0):
        return
    calculate_ways_to_get(av_coins, goal - av_coins[-1], current_solution + (av_coins[-1],), overall_set)
    calculate_ways_to_get(av_coins[:-1], goal, current_solution, overall_set)


@lru_cache(maxsize=None)    
def count_ways(av_coins, goal):
    if (goal == 0):
        return 1
    if(goal < 0 or len(av_coins) == 0):
        return 0
    return count_ways(av_coins, goal - av_coins[-1]) + count_ways(av_coins[:-1], goal)
    
def main():
    global sol_count
    start = clock()
    coins = available_coins()
    over_sol = set()
    goal = goal_sum()
    all_ways = count_ways(coins, goal)
    #print ("All solutions: " , sorted(over_sol, reverse=True))
    print ("\nNumber of solutions: " , all_ways)
    print ('all_ways clocked at', 'Time: ', str(clock() - start)+'s')
    print(count_ways.cache_info())
    

if __name__ == "__main__":
    main()
