#!/usr/bin/env python3

import sys

def LineIntersect(a, b):
  i, j = a.split("-")
  m, n = b.split("-")

  if i < m and j < n:
    return False
  elif i > m and j > n:
    return False

  return True

def Intersect(new_pair, chosen_pairs):
  for i in range(0, len(chosen_pairs)):
    if LineIntersect(chosen_pairs[i], new_pair):
      return True
  return False

def process_word(
  alignment_filename,
  word_file,
  pron_file,
):
  alignment_file = open(alignment_filename)

  for line in alignment_file:
    pairs  = line.split()
    with open(word_file) as f:
      chars  = f.readline().split()
    with open(pron_file) as f:
      phones = f.readline().split()

    start = 0

    intervals = [0]
    i = start
    while i < len(pairs):
      chosen_pairs = []
      chosen_pairs.append(pairs[i])

      if i + 1 == len(pairs):
        break

      for j in range(i + 1, len(pairs)):
        if Intersect(pairs[j], chosen_pairs):
          chosen_pairs.append(pairs[j])
        else:
          intervals.append(j)
          i = j
          break

      if (j == len(pairs) - 1):
        break


    intervals.append(len(pairs))

    ans = ""
    for i in range(1, len(intervals)):
      begin = int(pairs[intervals[i-1]].split("-")[0])
      end = len(chars)
      if intervals[i] < len(pairs):
        end = int(pairs[intervals[i]].split("-")[0])

      for j in range(begin, end):
        index = j
        ans = ans + chars[index]
      ans = ans + " "

    print(ans)
  alignment_file.close()

if __name__ == "__main__":
  alignment_file, word_file, pron_file = sys.argv[1:]
  process_word(alignment_file, word_file, pron_file)
