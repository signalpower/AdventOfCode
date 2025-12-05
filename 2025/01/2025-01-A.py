import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <inputfile>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    inputdata = f.read()

pos = 50
matches = 0
for line in inputdata.split("\n"):
  if len(line) > 1:
    dir = line[0]
    num = int(line[1:])
    matches += num // 100
    if dir == 'L':
      pos = (pos - num) % 100
    else:
      pos = (pos + num) % 100
    if pos == 0:
      matches += 1

print("Password is: ", matches)
