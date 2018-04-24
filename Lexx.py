#!/bin/python

import os.path

scriptDir = os.path.dirname(os.path.abspath(__file__))
modServices = []
modResponders = []
mods = []
thisMod = 0
debug = 0

#Load Plugins
for file in os.listdir(scriptDir + "/modules/"):
    if (file[-3:] == ".py" and file != "__init__.py"):
        thisMod = __import__("modules." + ".".join(file.split(".")[0:-1]), fromlist=['*'])
        print ("debug: imported %s" % thisMod.modName)
        if (thisMod.isResponder == True):
            modResponders.append(thisMod)

#Find Best Plugin for Response
def findBestMatchedPlugin(strinput):
    isMatch = []
    for mod in modResponders:
        isMatch.append(mod.matchStat(strinput))
        if debug == 1:
            print(mod.modName + ": " + str(mod.matchStat(strinput)))
    return modResponders[isMatch.index(max(isMatch))]

#User Prompt
print ("Lexx:   Welcome.")
while True:
    uinp = input(">>      ")
    print(findBestMatchedPlugin(uinp).getResponse(uinp))
