#!/usr/bin/python

import sys
import math
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # edge case
  if n < 1:
    return 1
  # elif n == 2:
  #   return 2
  # what is base case? when will recursion stop
  # find min and max amount of eating methods
  
  poss_list = []
  j = 0
  while sum(poss_list) < n:
    
  # max_e = n
  
  # if n % 2 > 0:
  #   mid_e = n // 2 + 1
  # elif n % 2 == 0:
  #   mid_e = n / 2
  
  # if n % 3 > 0 and n > 3:
  #   min_e = n // 3 + 1
  # elif n % 3 == 0:
  #   min_e = n / 3
  # elif n == 2:
  #   min_e = mid_e
  # else:
  #   min_e = max_e
  
  # print(eating_cookies(n - 1), n, 'recursion')
  return math.factorial(n) // (math.factorial(4) * math.factorial(n - 4))

print(eating_cookies(10), 'from function')
 
  



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')