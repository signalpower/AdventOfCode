import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <inputfile>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    inputdata = f.read()

idsum = 0
for idrange in inputdata.split(","):
  idrangesplit = idrange.split("-")

  for id in range(int(idrangesplit[0]), int(idrangesplit[1])+1, 1):
    idstr = str(id)
    if len(idstr)%2 == 0:
      middle = len(idstr) // 2
      if idstr[:middle] == idstr[middle:]:
        idsum += id

print("Answer: ", idsum)
