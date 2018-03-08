import os

# Get src patker
with open('src.patker') as file:
    lines = file.readlines()
lines = [x.strip() for x in lines]

# List where all output goes
out = []
curHard = [None]
path = os.path.dirname(os.path.realpath(__file__))

def checkHard(line):
    # Handle creating hards
    if line[:5] == 'hard ':
        dec = line[5: ]
        hardName = dec[:dec.find(' ')]
        dec = dec[dec.find(' ') + 1:]
        with open(hardName + '.hard', 'w') as newHard:
            newHard.write(dec)
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
        if curHard[0] != None:
            out.append(curHard[0])
# Parse Patker code
for line in lines:
    curHard = [None]
    checkHard(line)
    checkShow(line)

# remove hards
files = os.listdir(path)
for i in files:
    if i.endswith('.hard'):
        os.remove(path + '/' + i)
print(out)
