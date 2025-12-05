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
    for i in range(1, (len(idstr)//2)+1, 1):
      if len(idstr)%i == 0:
        teststr = idstr[:i] * (len(idstr) // i)
        if idstr == teststr:
          idsum += id
          break

print("Answer: ", idsum)
