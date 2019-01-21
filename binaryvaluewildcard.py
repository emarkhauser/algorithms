# Returns a list of all possible values for binary numbers where "?" is a wild card
def makebinary(instring):
    
    def addStrToList(stringlist, addedChar):
        newlist = list(stringlist)
        for x in range(len(newlist)):
            newlist[x] = newlist[x] + addedChar
        return newlist
    
    binlist = [""]
    
    for x in range(len(instring)):
        if instring[x] in ["0","1"]:
            binlist = addStrToList(binlist, instring[x])
        elif instring[x] == "?":
            binlist = addStrToList(binlist, "0") + addStrToList(binlist, "1")
        else:
            return(["Value other than 0, 1, ? detected"])
    return(binlist)

print(makebinary("0?1"))
