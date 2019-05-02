#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  plays = [['rock'], ['paper'], ['scissors']]
  if n == 1:
    return plays

  rounds = []
  rps = rock_paper_scissors(n - 1)
  for i in plays:
    for j in rps:
      rounds.append(i + j)
  return rounds


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')