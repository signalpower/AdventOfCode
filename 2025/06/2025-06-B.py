import sys

debug = False
if len(sys.argv) < 2:
  print("Usage python ",sys.argv[0], "<input file>")
  sys.exit(1)

try:
  with open(sys.argv[1], "r") as f:
    inputdata = f.read()
except FileNotFoundError:
  print("Error: The file was not found.")
  sys.exit(1)

rows = [line.rstrip("\n") for line in inputdata.splitlines()]
width = max(len(r) for r in rows)
matrix = [list(r.ljust(width)) for r in rows]
height = len(matrix)

if debug:
  print("\n[DBG] === MATRIX ({} rows × {} cols) ===".format(height, width))
  for row in matrix:
    print("".join(row))

empty_cols = [
  all(matrix[row][col] == " " for row in range(len(matrix)))
  for col in range(width)
]

if debug:
  print("[DBG] --- EMPTY COLS ---")
  for col in range(width):
    if empty_cols[col]:
      print("T", end='')
    else:
      print("F", end='')
  print(" ")

tot = 0
start = 0
end = 0


for col in range(width+1):
  is_empty = (col == width) or empty_cols[col]

  if is_empty:
    if end > start:

      if debug:
        print("\n[DBG] === BLOCK DETECTED: cols {}..{} ({} wide) ===".format(start, end-1, end-start))

      block = [ row[start:end] for row in matrix]
      num_block = block[:-1]
      ops_block = block[-1]

      if debug:
        print("\n[DBG] -- RAW BLOCK --")
        for r in block:
          print("".join(r))

      num_rot = list(map(list, zip(*num_block)))[::-1]

      if debug:
        print("\n[DBG] --  ROTATED (NUM_ROT) --")
        for r in num_rot:
          print("".join(r))

      num_int = []

      if debug:
        print("\n[DBG] -- PARSED NUMBERS --")

      for r in num_rot:
        s = "".join(ch for ch in r if ch.isdigit())
        if debug:
          print("[DBG]    digits:", repr(s))
        if s:
          num_int.append(int(s))
      if debug:
        print("[DBG]    integers:", num_int)
        print("\n[DBG] -- OPERATOR BLOCK --")
        print("".join(ops_block))
      
      if "*" in ops_block:
        if debug:
          print("[DBG]    Multiplication")
        subtot = 1
        for num in num_int:
          subtot *= num
      else:
        if debug:
          print("[DBG]    Addition")
        subtot = sum(num_int)
      if debug:
        print("[DBG] -- Subtotal =", subtot)
      tot += subtot
      start = end
  end += 1

print("Answer is: ", tot)
