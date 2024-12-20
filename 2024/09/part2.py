with open("input.txt", "r") as inputfile:
    flist = list(inputfile.read().strip())

fid = 0
dmap = []

for ind, fdata in enumerate(flist):
    f = int(fdata)
    if ind % 2 == 0:
        for x in range(f):
            dmap.append(fid)
        fid += 1
    else:
        for x in range(f):
            dmap.append(-1)

fileidprocessed = []
for fileEnd in reversed(range(len(dmap))):
    if dmap[fileEnd] >= 0:
        fileID = dmap[fileEnd]
        fileStart = fileEnd
        while dmap[fileStart-1] == fileID:
            fileStart -= 1
        fileSize = fileEnd - fileStart + 1
        if fileID not in fileidprocessed:
            fileidprocessed.append(fileID)
            for freeStart in range(0, fileStart):
                if dmap[freeStart] == -1:
                    freeEnd = freeStart
                    while dmap[freeEnd+1] == -1:
                        freeEnd += 1
                    freeSize = freeEnd - freeStart + 1
                    if freeSize >= fileSize:
                        for x in range(fileSize):
                            dmap[freeStart+x], dmap[fileStart+x] = dmap[fileStart+x], dmap[freeStart+x]
                        break

checksum = 0
for i, d in enumerate(dmap):
    if d > 0:
        checksum += i*d

print("The checksum is: " + str(checksum))

