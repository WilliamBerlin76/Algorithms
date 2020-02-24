#!/usr/bin/python

import argparse

def find_max_profit(prices):

  greatest_diff = 0
  for i in range(len(prices)):
    for j in range(len(prices[i:])):

      if greatest_diff <= 0 and prices[i] != prices[-1]:
        if greatest_diff == 0:
          greatest_diff = prices[j + i] - prices[i]

        elif greatest_diff < 0:
          if prices[j + i] - prices[i] > greatest_diff:
            greatest_diff = prices[j + i] - prices[i]
        
      elif prices[j + i] >= prices[i] and prices[i] != prices[-1]:
        if prices[j + i] - prices [i] > greatest_diff:
          greatest_diff = prices[j + i] - prices[i]
    
  return greatest_diff

  # more efficient attempt below

  # low = 0
  # high = 0
  # low_so_far = prices[0]
  # high_so_far = prices[0]
  # greatest_diff = 0
  # i = 0

  # while i < len(prices) - 1:
    
  #   if prices[i] < low_so_far and high == 1:
  #     low_so_far = prices[i]
  #     high_so_far = prices[i]
  #     high = 0
  #     i += 1
  #   elif prices[i] < low_so_far and high == 0:
  #     low_so_far = prices[i]
  #     high_so_far = prices[i]
  #     high = 1
  #     i += 1
  #   elif prices[i] > high_so_far :
  #     high_so_far = prices[i]
  #     high = 1
  #     i += 1
  #   else:
  #     i += 1

  # print(high_so_far,low_so_far)
  
  # return high_so_far - low_so_far

print(find_max_profit([100, 90, 80, 50, 20, 10]))
print(find_max_profit([10, 7, 5, 8, 11, 9]))
print(find_max_profit([1050, 270, 1540, 3800, 2]))
print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))