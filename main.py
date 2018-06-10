file = open("testfile.txt", "r")
string = file.readlines()
grammers = []
def finder(c):
    for i in range(0,len(grammers)):
        if(c in grammers[i][0]):
            if(not any(x.isupper() for x in grammers[i][1])):
                return grammers[i][1]
    return 0
for str in string :
    grl = [str[0],str[1:len(str)].replace('\n','')]
    grammers.append(grl)
##lambda production
for i in range(0,len(grammers)):
    if('l' in grammers[i][1]):
        c = grammers[i][0]
        del grammers[i]
        for j in range (0,len(grammers)):
            str2 = grammers[j]
            if c in str2[1] :
                grammers.append([str2[0],str2[1].replace(c,'')])
##unit production
deleted = []
for j in range(0,len(grammers)):
    for c in grammers[j][1]:
        done = finder(c)
        if(done != 0):
            deleted.append(j)
            grammers.append([grammers[j][0],grammers[j][1].replace(c,'') + done])
for a in range(0,len(deleted)):
    del grammers[deleted[a] - a]
##useless production
used = []
used.append('S')
def findindex(c):
    for i in range(0,len(grammers)):
        if(c == grammers[i][0]):
            return i
def grammercheck(i):
    for c in grammers[i][1]:
        if(c.isupper()):
            used.append(c)
            return grammercheck(findindex(c))
# for strs in grammers:
#     for c in strs[1]:
#         if c.isupper():
#             used.append(c)
shoulddelete = []
for k in range(0,len(grammers)):
    char = grammers[k][0]
    if not char in used:
        shoulddelete.append(k)
for en in range(0,len(shoulddelete)):
    del grammers[shoulddelete[en] - en]
print(grammers)
for state in grammers:
    print(state[0] + "->" + state[1].replace('l','λ'))