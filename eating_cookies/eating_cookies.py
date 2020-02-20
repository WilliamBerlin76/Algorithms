#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# 0: eat 0 ckies 1 time
# 1: eat 1 cookie 1 time
# 2: eat 1 cookie 1 time, eat 1 coookie 1 time
# 2: eat 2 cookies
# 3: eat 1 cookei 1 time, eat 1 cookie 1 time, eat 1 cookie 1 time
# 3: eat 2, then 1
# 3: eat 1, then 2
# 3: eat 3
cache = {}

def eating_cookies(n, cache=None):
  
  if n < 0:
    return 0
  elif n <= 1:
    return 1
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if cache is None:
      cache = {}
    value = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    cache[n] = value
    return value

  # elif n == 2:
  #   return 2
  # what is base case? when will recursion stop
  # find min and max amount of eating methods
  
  # while sum(poss_list) < n:
    
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
  
# print(eating_cookies(10), 'from function')
 
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')