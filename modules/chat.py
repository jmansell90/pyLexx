modName = "chat"
isResponder = True

inqWords = ["WHO", "WHAT", "WHEN", "WHERE", "WHY", "HOW", "IS", "DOES", "ARE", "DO", "ISN'T", "AREN'T", "DOESN'T"]
greetWords = ["HELLO", "HI", "HEY"]

def matchStat(uinput):
    return 1

def getResponse(uinput):
    arrInput = uinput.split(" ")
    if "LEXX" in arrInput[0].upper():
        arrInput.remove(arrInput[0])
    if arrInput[0].upper() in inqWords:
        return "Lexx: I can't answer questions yet."
    if arrInput[0].upper() in greetWords:
        return "Hello Cryo, how are you?"
    else:
        return "Lexx:   I'm not sure what to say..."

class ModuleClass:
    def run():
        print ("test module 1 is running")
    def getTriggers():
        return "*"
