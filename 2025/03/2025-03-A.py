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
    best = 0
    for i in range(len(line)-1):
      for j in range(i+1, len(line)):
        value = int(line[i] + line[j])
        if value > best:
          best = value
    total += best
print("Answer is: ",total)
