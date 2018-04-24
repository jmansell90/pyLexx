modName = "download"
isResponder = True

def matchStat(uinput):
    if "DOWNLOAD " in uinput.upper():
        return 100
    else:
        return 0

def getResponse(uinput):
    print("Lexx:   Ok, let me search for " + uinput.split("download ",1)[1])

class ModuleClass:
    def run():
        print ("test module 1 is running")
    def getTriggers():
        return "*"
