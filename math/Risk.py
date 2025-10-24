import random

def rollAttacker():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll3 = random.randint(1,6)
    aDice = [roll1,roll2,roll3]
    return aDice
def rollDefender():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    dDice = [roll1,roll2]
    return dDice

aPoints = 0
dPoints = 0
totalRolls = 1000000
for i in range(totalRolls):
    aDice = rollAttacker()
    dDice = rollDefender()
    aDice.sort()
    dDice.sort()
    if(aDice[2] > dDice[1]):
        aPoints += 1
    else:
        dPoints += 1
    if(aDice[1] > dDice[0]):
        aPoints += 1
    else:
        dPoints += 1
print(aPoints)
print(dPoints)
winPercentage = (aPoints/(totalRolls*2)) * 100
print("Attackers Win Percentage : ", round(winPercentage,2), "%")