import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <inputfile>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    inputdata = f.read()

total = 0
for line in inputdata.split("\n"):
  n = len(line)
  if n > 1:
    result = []
    rem = 12
    start = 0
    while rem > 0:
      end = n - rem + 1
      digit = max(line[start:end])
      pos = line.index(digit, start, end)
      result.append(digit)
      start = pos + 1
      rem -= 1

    total += int("".join(result))

print("Answer is: ",total)

