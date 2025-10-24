import random

counter = 0
wins = 0
loses = 0

def roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    return total

while counter < 1000000:
    counter +=1
    #print(f"Game number {counter}")
    total = roll()

    if total == 7 or total == 11:
        wins += 1
    elif total == 2 or total == 3 or total == 12:
        loses += 1
    else:
        point = total
        while True:
            
            total = roll()
            if total == point:
                wins +=1
                break
            elif total == 7:
                loses +=1
                break
    

print(f"Total wins: {wins}")
print(f"Total loses: {loses}")
percentage = (wins / 1000000) * 100
print(f"Chance at winning: {percentage}")

