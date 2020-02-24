#!/usr/bin/python

import sys
# create cache:
cache = []
# the cache can store all of the ways to make change for the coin values
def making_change(amount, denominations):
  if amount == 0:
    return 1
  # initialize cache: position of num == amount of cents, value is the number of ways to make change for it
  # cache = [0] * amount
  # cache[0] = 1
  # cache[1] = 1
  # for higher_amount in range(coin, amount + 1)

  # print(cache)
  if amount < 0:
    return 0
  if len(denominations) <= 0 and amount > 0:
    return 0
  else:
    value = making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])
    return value


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")