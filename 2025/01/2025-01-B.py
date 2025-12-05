import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <inputfile>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    lines = [line.strip() for line in f if line.strip()]

pos = 50
hits = 0

for line in lines:
  dir = line[0]
  num = int(line[1:])
  old = pos

  # Right rotation
  if dir == 'R':
    # find k such that (old + k) % 100 == 0
    first = (100 - old) % 100
  else:
    # Left rotation: (old - k) % 100 == 0 → k == old mod 100
    first = old % 100

  # If the first occurrence is within [1..num], count it + multiples of 100
  if first != 0:       # if first == 0, that means k=0 → not a click
    if first <= num:
      hits += 1 + (num - first) // 100
  else:
    # special case: first hit would be k=0 → next is k=100
    if num >= 100:
      hits += 1 + (num - 100) // 100

  # compute new final position
  if dir == 'R':
    pos = (old + num) % 100
  else:
    pos = (old - num) % 100

print("Password is:", hits)
