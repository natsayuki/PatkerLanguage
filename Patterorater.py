import os
import re

# Get src patker
with open('src.patker') as file:
    lines = file.readlines()
lines = [x.strip() for x in lines]

# List where all output goes
out = []
curHard = [None]
curLit = [None]
curLitType = [None]
path = os.path.dirname(os.path.realpath(__file__))


def checkLiteral(line):
    try:
        int(line)
        del curLit[0]
        del curLitType[0]
        curLit.append(line)
        curLit.append('num')
        done = True
    except:
        done = False
    if not done:
        if line.startswith('"') and line.endswith('"'):
            del curLit[0]
            restline = line[line.find('"') + 1:line[line.find('"') + 1:].find('"') + 1]
            curLit.append(restline)
            del curLitType[0]
            curLitType.append("Words")
        if line.startswith("'") and line.endswith("'"):
            del curLit[0]
            restline = line[line.find("'") + 1:line[line.find("'") + 1:].find("'") + 1]
            curLit.append(restline)
            del curLitType[0]
            curLitType.append("Words")
        regex = re.compile('[0-9]+ \+ [0-9]+')
        if regex.match(line):
            del curLit[0]
            curLit.append(eval(line))
def checkHard(line):
    # Handle creating hards
    if line[:5] == 'hard ':
        dec = line[5: ]
        hardName = dec[:dec.find(' ')]
        dec = dec[dec.find(' ') + 1:]
        checkLiteral(dec)
        curVar = curLit[0]
        if curLit[0] == None:
            checkHard(dec)
            curVar = curHard[0]
        with open(hardName + '.hard', 'w') as newHard:
            newHard.write(str(curVar))
            # Handle showing hards
    if line[:7] == 'recall ':
        hardName = line[7: ]
        try:
            with open(hardName + '.hard', 'r') as hard:
                del curHard[0]
                curHard.append(hard.read())
        except:
            out.append('ERROR! No hard ' + hardName)
def checkShow(line):
    if line[:5] == 'show ':
        checkHard(line[5:])
        checkLiteral(line[5:])
        if curHard[0] != None:
            out.append(curHard[0])
        elif curLit[0] != None:
            out.append(curLit[0])
# Parse Patker code
for line in lines:
    curHard = [None]
    curLit = [None]
    curLitType = [None]
    checkHard(line)
    checkShow(line)

# remove hards
files = os.listdir(path)
for i in files:
    if i.endswith('.hard'):
        os.remove(path + '/' + i)
print(out)
