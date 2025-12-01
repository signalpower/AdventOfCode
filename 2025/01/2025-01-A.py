#import re

with open("input_test.txt", "r") as inputfile:
  inputdata = inputfile.read()

MIN = 0
MAX = 99

pos = 50
matches = 0
for line in inputdata.split("\n"):
  if len(line) > 1:
    dir = line[0]
    num = int(line[1:])
    print(pos, " || ", line, "  || Dir: ", dir, " Num:", num)
    if dir == 'L':
      pos = pos - num
      if pos < MIN:
        pos = MAX - abs(pos)
    elif dir == 'R':
      pos = pos + num
      if pos > MAX:
        pos = MIN + pos - MAX
    else:
      print("Dir neither 'L' or 'R': ", dir)
    if pos == 0:
      matches += 1

print("Password is: ", matches)
