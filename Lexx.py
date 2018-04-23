#!/bin/python

import os.path

scriptDir = os.path.dirname(os.path.abspath(__file__))
mods = []
thisMod = 0

#Load Plugins
for file in os.listdir(scriptDir + "/modules/"):
    if (file[-3:] == ".py" and file != "__init__.py"):
        thisMod = __import__("modules." + ".".join(file.split(".")[0:-1]), fromlist=['*'])
        print ("debug: imported %s" % thisMod.modName)
        if (thisMod.enable == True):
            mods.append(thisMod)

#User Prompt
print ("Lexx:   Welcome.")
while True:
    uinp = input(">>      ")
