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

#result = 0

linedata = {}
for line in inputdata.splitlines():
  ls = line.split(":")
  linedata[ls[0]] = ls[1]

def countout (data):
  if data.strip() == "out":
    return 1
  else:
    total = 0
    for newdata in data.split():
      total += countout(linedata[newdata])
    return total

result = countout(linedata["you"])

print("Answer is: ", result)
