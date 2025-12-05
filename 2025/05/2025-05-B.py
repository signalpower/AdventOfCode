import sys

if len(sys.argv) < 2:
  print("Usage python ",sys.argv[0], "<input file>")
  sys.exit(1)

try:
  with open(sys.argv[1], "r") as f:
    inputdata = f.read()
except FileNotFoundError:
  print("Error: The file was not found.")
  sys.exit(1)

#Read data
ranges = []
for line in inputdata.split("\n"):
  s = line.strip()
  if not s:
    continue

  if "-" in s:
    linesplit = line.split('-')
    ranges.append((int(linesplit[0]),int(linesplit[1])))

ranges.sort()

merged = []
start, end = ranges[0]

for a, b in ranges[1:]:
  if a <= end + 1:
    end = max(end,b)
  else:
    merged.append((start,end))
    start, end = a, b
merged.append((start, end))

total = sum(b - a + 1 for a, b in merged)

print("Answer is: ", total)
