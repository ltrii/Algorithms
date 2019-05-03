#!/usr/bin/python

import sys

cache = {}
def making_change(amount, denominations):
  return coin_combos(amount, denominations, len(denominations)-1)

def coin_combos(amount, denominations, n):
  if amount == 0:
    return 1
  try:
    return cache[(amount, n)]
  except:
    pass
  if amount < 0 or n < 0:
    return 0
  coin = denominations[n]
  inc = coin_combos(amount-coin, denominations, n)
  out = coin_combos(amount, denominations, n-1)
  result = inc + out
  cache[(amount, n)] = result
  return result


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")