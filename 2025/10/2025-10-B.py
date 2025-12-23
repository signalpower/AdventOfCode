import sys
import re
#from fractions import Fraction
#import itertools
import math
import heapq


####


from z3 import *

def solve_line(jolts, button_patterns):
  """
  Solve:
      sum_i x[i] * button_patterns[i][p] == jolts[p]
  for all positions p,
  with x[i] >= 0 integers,
  minimizing sum(x[i]).

  jolts: tuple[int]        (target values)
  button_patterns: list[tuple[int]]  (0/1 for each position)
  """

  P = len(jolts)
  N = len(button_patterns)

  opt = Optimize()

  # Create integer variables: x_0 ... x_(N-1)
  xs = [Int(f"x{i}") for i in range(N)]

  # All xs[i] >= 0
  for xi in xs:
    opt.add(xi >= 0)

  # Per-position constraints
  for p in range(P):
    opt.add(
      Sum(xs[i] * button_patterns[i][p] for i in range(N)) == jolts[p]
    )

  # Objective: minimize total number of presses
  total_presses = Sum(xs)
  opt.minimize(total_presses)

  # Solve
  result = opt.check()
  if result != sat:
    raise ValueError("No solution found for line (unexpected).")

  model = opt.model()
  return sum(model[xs[i]].as_long() for i in range(N))


####


def make_toggle_mask(size, indices):
  mask = 0
  for i in indices:
    mask |= (1 << i)
  return mask


if len(sys.argv) < 2:
  print("Usage python ",sys.argv[0], "<input file>")
  sys.exit(1)

try:
  with open(sys.argv[1], "r") as f:
    inputdata = f.read()
except FileNotFoundError:
  print("Error: The file was not found.")
  sys.exit(1)

lines = [line for line in inputdata.splitlines() if line.strip()]
total_lines = len(lines)

pattern = re.compile(r"\[([.#]+)\]\s+((?:\([0-9,]*\)\s*)+)\{([0-9,]+)\}", re.VERBOSE)

result = 0
for idx, line in enumerate(lines, start=1):
  print(f"Processing line {idx} of {total_lines}")
  matches = pattern.findall(line)
  if not matches:
    raise ValueError("Line format wrong")
  lights_raw, toggles_raw, jolts_raw = matches[0]
  jolts = tuple(int(x) for x in jolts_raw.split(','))

  M = len(jolts)
  toggle_vectors = []
  groups = re.findall(r"\(([^)]*)\)", toggles_raw)
  toggle_index_lists = [
    [int(x) for x in g.split(',') if x]
    for g in groups
  ]
  for idxs in toggle_index_lists:
    vec = [0] * M
    for i in idxs:
      vec[i] = 1
    toggle_vectors.append(tuple(vec))
#  toggles_sorted = sorted(toggle_vectors, key=lambda p: sum(p), reverse=True)
#  button_presses = solve_line(jolts, toggles_sorted)
  button_presses = solve_line(jolts, toggle_vectors)
  print(f"    Button presses: {button_presses}")
  result += button_presses

print("Answer is: ", result)
