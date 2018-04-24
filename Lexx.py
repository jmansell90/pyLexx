#!/bin/python

import os.path

scriptDir = os.path.dirname(os.path.abspath(__file__))
tmpDir = scriptDir + "/lexx-tmp"

modServices = []
modResponders = []
mods = []
thisMod = 0
debug = 0

#Load Plugins
for folder in os.listdir(scriptDir + "/modules/"):
    for file in os.listdir(scriptDir + "/modules/" + folder + "/"):
        if (file[-3:] == ".py" and file != "__init__.py"):
            thisMod = __import__("modules." + folder + "." + ".".join(file.split(".")[0:-1]), fromlist=['*'])
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
print ("Lexx AI is Ready.")
while True:
    #Read In Pending
    for file in os.listdir(tmpDir + "/pending-in"):
        inmsg = []
        inmsg = open(tmpDir + "/pending-in/" + file).readlines()
        os.rename(tmpDir + "/pending-in/" + file, tmpDir + "/pending-proc/" + file)
        iusr = inmsg[0].strip("/n")
        imsg = inmsg[1]
        print(iusr + ": " + imsg)
        resp = open(tmpDir + "/pending-out/" + file, "w")
        resp.write(iusr)
        resp.write(findBestMatchedPlugin(imsg).getResponse(imsg))
        resp.close()
        os.remove(tmpDir + "/pending-proc/" + file)
    #Careful Cleanup

    #Send Pending Out
    for file in os.listdir(tmpDir + "/pending-out"):
        outmsg = []
        outmsg = open(tmpDir + "/pending-out/" + file).readlines()
        os.remove(tmpDir + "/pending-out/" + file)
        ousr = outmsg[0].strip("/n")
        omsg = outmsg[1]
        print("Lexx(To " + ousr + "):  " + omsg)
#    uinp = input(">>      ")
#    print(findBestMatchedPlugin(uinp).getResponse(uinp))
