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
ingredients = []
for line in inputdata.split("\n"):
  s = line.strip()
  if not s:
    continue

  if "-" in s:
    linesplit = line.split('-')
    ranges.append((int(linesplit[0]),int(linesplit[1])))
  if s.isdigit():
    ingredients.append(int(s))

fresh = 0
for i in ingredients:
  for a, b in ranges:
    if a <= i <= b:
      fresh += 1
      break

print("Answer is: ", fresh)
