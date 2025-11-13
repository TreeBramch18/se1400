import random

N = input("Give me a number, Ill tell you if it's prime \r\n")
N = int(N)
M = N-1

S = 0
T = M

while T % 2:
    T //= 2
    S += 1

M = N-1
T = int(T)
R = random.randint(2,M-1);
quickBool = False;

if(pow(R,T,N)==1):
    print("Your Number is most likely a Prime")
elif(S == 0):
    print("Your Number is not prime")

else:
    for i in range(S):
        if(pow(R,T,N)==M):
            quickBool == True
            print("Your Number is most likely a Prime")
        elif(i != S):
            T *= 2;

    if(quickBool == False):
        print("Your Number is not prime")
