elments = [1, 2, 3, 4, 5]







print("Combinations no repetition :")

for i in range(len(elments)):
    for j in range(i+1, len(elments)):
        for k in range(j+1, len(elments)):
            print(elments[i], elments[j], elments[k])

print("Combinations repetition :")

for i in range(len(elments)):
    for j in range(i, len(elments)):
        for k in range(j, len(elments)):
            print(elments[i], elments[j], elments[k])

print("Permutations No Repetition :")

for i in range(len(elments)):
    for j in range(len(elments)):
        if j != i:
            for k in range(len(elments)):
                if k != i and k != j:
                    print(elments[i], elments[j], elments[k])

print("Permutations repetition :")

for i in range(len(elments)):
    for j in range(len(elments)):
        for k in range(len(elments)):
            print(elments[i], elments[j], elments[k])