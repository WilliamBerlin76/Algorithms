#!/usr/bin/python

import sys
# notice, the first n-1 items in each list repeats itself 3 times
# len of expected output always 3 ^ n
def rock_paper_scissors(n):
  #list of rps plays
  rps_options = ['rock', 'paper', 'scissors']
  all_possibilities = []
  # base case - inner arrays should be no longer than n
  if n == 0:
    return [[]]
    
  # hint for defining an inner recursive function 
  def inner_recurse(cur_n, arr = []):
    if cur_n < 1:
      return all_possibilities.append(arr)
    for choice in rps_options:
      inner_recurse(cur_n - 1, arr + [choice])
  
  inner_recurse(n)
  return all_possibilities
  

  # need a list of lists, inner list always have len n

  # output not the amount of permutations but the list of actual permutations

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')



# ideas below

  # if round_list in cache:
  #   return rock_paper_scissors(n)
  # if len(round_list) == n and round_list not in cache:
  #   cache.append(round_list)
  #   return rock_paper_scissors(n)
  
  # elif len(round_list) < n: