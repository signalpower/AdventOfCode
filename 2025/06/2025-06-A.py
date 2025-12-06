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
data = []
for line in inputdata.split("\n"):
  con = []
  s = line.strip()
  if not s:
    continue
  for t in s.split():
    if t.isdigit():
      con.append(int(t))
    else:
      con.append(t)
  data.append(con)

tot = 0
opry = len(data) - 1

for x in range(len(data[0])):
  if data[opry][x] == "*":
    subtot = 1
  else:
    subtot = 0
  for y in range(len(data)-1):
    if data[opry][x] == "*":
      subtot *= data[y][x]
    else:
      subtot += data[y][x]
  tot += subtot

print("Answer is: ", tot)
