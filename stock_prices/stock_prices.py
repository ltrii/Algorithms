#!/usr/bin/python

import argparse

def find_max_profit(prices):
  sorted_prices = sorted(prices)
  highest = sorted_prices[-1]
  count = 0
  def find_low(l):
    if prices.index(highest) > prices.index(l):
      lowest = l
      return highest - lowest
    if prices.index(highest) < prices.index(l):
      nonlocal count
      count = count + 1
      return find_low(sorted_prices[count])
  return find_low(sorted_prices[0])


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))