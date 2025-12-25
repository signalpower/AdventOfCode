import sys

if len(sys.argv) < 2:
  print("Usage: python ",sys.argv[0], "<input file>")
  sys.exit(1)

try:
  with open(sys.argv[1], "r") as f:
    inputdata = f.read()
except FileNotFoundError:
  print("Error: The file was not found.")
  sys.exit(1)

linedata = {}
for line in inputdata.splitlines():
  ls = line.split(":")
  linedata[ls[0]] = ls[1]

cache = {}
def countout (idx, seen_fft=False, seen_dac=False):
  key = (idx, seen_fft, seen_dac)
  if key in cache:
    return cache[key]
  if linedata[idx].strip() == "out":
    if seen_fft and seen_dac:
      cache[key] = 1
      return 1
    else:
      cache[key] = 0
      return 0
  else:
    total = 0
    if idx == "fft":
      seen_fft = True
    if idx == "dac":
      seen_dac = True
    for newidx in linedata[idx].split():
      total += countout(newidx, seen_fft, seen_dac)
    cache[key] = total
    return total

result = countout("svr")

print("Answer is: ", result)
