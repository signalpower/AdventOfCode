import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <inputfile>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    inputdata = f.read()

total = 0
for line in inputdata.split("\n"):
  if len(line) > 1:
    result = []
    rem = 12
    start = 0
    while rem > 0:
      end = len(line) - rem + 1
      chunk = line[start:end]
      digit = max(chunk)
      pos = line.index(digit, start, end)
      result.append(digit)
      start = pos + 1
      rem -= 1

    total += int("".join(result))

print("Answer is: ",total)

