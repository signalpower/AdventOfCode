import sys
import re

def make_toggle_mask(size, indices):
  mask = 0
  for i in indices:
    mask |= (1 << i)
  return mask

def to_bitmask(bools):
  mask = 0
  for i, v in enumerate(bools):
    if v:
      mask |= (1 << i)
  return mask

def parse_toggle_masks(toggles_raw, size):
  groups = re.findall(r"\(([^)]*)\)", toggles_raw)
  toggle_index_lists = [[int(x) for x in g.split(',') if x] for g in groups]
  return [make_toggle_mask(size, idxs) for idxs in toggle_index_lists]

def solve_line(final_mask, toggle_masks):
  N = len(toggle_masks)
  best_count = None
  best_subsets = []

  for subset in range(1 << N):
    state = 0
    for i in range(N):
      if subset & (1 << i):
        state ^= toggle_masks[i]

    if state == final_mask:
      c = subset.bit_count()
      if best_count is None or c < best_count:
        best_count = c
        best_subsets = [subset]
      elif c == best_count:
        best_subsets.append(subset)

  return best_count, best_subsets


if len(sys.argv) < 2:
  print("Usage python ",sys.argv[0], "<input file>")
  sys.exit(1)

try:
  with open(sys.argv[1], "r") as f:
    inputdata = f.read()
except FileNotFoundError:
  print("Error: The file was not found.")
  sys.exit(1)

pattern = re.compile(r"\[([.#]+)\]\s+((?:\([0-9,]*\)\s*)+)\{([0-9,]+)\}", re.VERBOSE)

result = 0
for line in inputdata.splitlines():
  matches = pattern.findall(line)
  if not matches:
    raise ValueError("Line format wrong")
  lights_raw, toggles_raw, jolts_raw = matches[0]
  lights = [ch == '#' for ch in lights_raw]
  final_mask = to_bitmask(lights)
  toggle_masks = parse_toggle_masks(toggles_raw, len(lights))
  best_count, best_subsets = solve_line(final_mask, toggle_masks)
  result += best_count

print("Answer is: ", result)
