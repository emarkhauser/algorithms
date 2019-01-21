# How do you find the duplicates in a list? 
def duplicate(inlist):
    duplicate = []
    newlist = inlist
    newlist.sort()
    for x in range(len(newlist)):
        if (newlist[x] == newlist[x-1]) and (x > 0) and newlist[x] not in duplicate:
            duplicate.append(newlist[x])
    print(duplicate)

duplicate(["2","1","1","3","2","40","3","4","4","4"])
