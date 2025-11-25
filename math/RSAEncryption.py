import MillersAlgorithm
import math

class RSA:
    def GenerateKeys(strOne, strTwo):
        alphabet1 = "abcdefghijklmnopqrstuvwxyz"
        revOne = reversed(strOne)
        revTwo = reversed(strTwo)
        
        baseIndex = 0
        numOne = 0;       
        for i in revOne:
            alpindex = alphabet1.index(i)
            numOne += alpindex * (26 ** baseIndex)
            baseIndex += 1
        
        baseIndex = 0
        numTwo = 0;
        for i in revTwo:
            alpindex = alphabet1.index(i)
            numTwo += alpindex * (26 ** baseIndex)
            baseIndex += 1

        hugeNumberForComparison = 10 ** 200
        if numOne < (hugeNumberForComparison) or numTwo < (hugeNumberForComparison):
            print("input strings are too short")
            quit()
        
        numOne %= hugeNumberForComparison
        numTwo %= hugeNumberForComparison

        if(numOne % 2 != 1):
            numOne += 1;
        if(numTwo % 2 != 1):
            numTwo += 1;

        while(not MillersAlgorithm.is_probable_prime(numOne)):
            numOne += 2
        while(not MillersAlgorithm.is_probable_prime(numTwo)):
            numTwo += 2

        numSum = numOne * numTwo # N
        numDif = (numOne-1)*(numTwo-1) # R
        # Find e – a 398 digit number that is relatively prime with r.
        numRel = (10 ** 398) + 1 # E

        while (not math.gcd(numDif, numRel) == 1):
            numRel += 2
        
        numInv = 0 # D
        # Find d – the inverse of e mod r. Python supports this directly with d=pow(e, -1, r).
        numInv = pow(numRel, -1, numDif)

        with open("public.txt", "w") as f:
            f.write(str(numSum) + "\n")
            f.write(str(numRel) + "\n")

        with open("private.txt", "w") as f:
            f.write(str(numSum) + "\n")
            f.write(str(numInv) + "\n")

    def Encrypt(input, output):
        fin = open(input,"rb")
        PlainTextBinary = fin.read()
        PlainText = PlainTextBinary.decode("utf-8")
        fin.close()

        alphabet2 = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        numBlock = 216

        blocks = []
        for i in range(0, len(PlainText), numBlock):
            blocks.append(PlainText[i:i + numBlock])

        numSum = 0;
        numRel = 0;

        with open("public.txt", "r") as f:
            numSum = int(f.readline().strip())
            numRel = int(f.readline().strip())
        
        outFile = open(output, "wb")

        for block in blocks:
            num = 0
            baseIndex = 0
            revBlock = reversed(block)

            for ch in revBlock:
                alpIndex = 0
                while ch != alphabet2[alpIndex]:
                    alpIndex += 1

                num += alpIndex * (70 ** baseIndex)
                baseIndex += 1
            cipher = pow(num, numRel, numSum)
            encoded = ""

            if cipher == 0:
                encoded = alphabet2[0]
            else:
                temp = cipher
                base70chars = []

                while temp > 0:
                    remainder = temp % 70
                    base70chars.append(alphabet2[remainder])
                    temp //= 70

                base70chars.reverse()

                for c in base70chars:
                    encoded += c
            encoded += "$"
            outFile.write(encoded.encode("utf-8"))
        
        outFile.close()

    def Decrypt(inputfile, outputfile):
        fin = open(inputfile, "rb")
        CipherTextBinary = fin.read()
        CipherText = CipherTextBinary.decode("utf-8")
        fin.close()

        alphabet2 = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        with open("private.txt", "r") as f:
            n = int(f.readline().strip())
            d = int(f.readline().strip())

        cipherBlocks = CipherText.split("$")
        if cipherBlocks[-1] == "":
            cipherBlocks.pop()

        fout = open(outputfile, "wb")

        for block in cipherBlocks:

            # Convert base 70 -> base 10
            num = 0
            baseIndex = 0
            revBlock = reversed(block)

            for ch in revBlock:
                alpIndex = 0
                while ch != alphabet2[alpIndex]:
                    alpIndex += 1
                num += alpIndex * (70 ** baseIndex)
                baseIndex += 1

            # RSA decrypt
            plainNum = pow(num, d, n)

            # Convert base 10 -> base 70
            decoded = ""
            if plainNum == 0:
                decoded = alphabet2[0]
            else:
                temp = plainNum
                chars = []
                while temp > 0:
                    remainder = temp % 70
                    chars.append(alphabet2[remainder])
                    temp //= 70
                chars.reverse()
                for c in chars:
                    decoded += c

            # If block decoded is empty, fill with first alphabet character to preserve length
            if decoded == "":
                decoded = alphabet2[0]

            # Write to file
            fout.write(decoded.encode("utf-8"))

        fout.close()


def main():
    rsa = RSA()

    strOne = "hellotheremynameismarkiplierandtodaywewillbeplayingfivenightsatfreddysthisgameisamascothorrorgamewithlotsofjumpscareswewillbedefendingourofficefromatoybearatoyhcickenatoybunnyandatoyfox"
    strTwo = "accordingtoallknownlawsofaviationthereisnowayabeeshouldbeabletoflyitswingsaretoosmalltogetitsfatlittlebodyoffthegroundthebeeofcoursefliesanyways"
    RSA.GenerateKeys(strOne, strTwo)
    RSA.Encrypt("original.txt", "encrypted.txt")
    RSA.Decrypt("encrypted.txt", "decrypted.txt")

    print("Decryption complete. Output written to decrypted.txt")



if __name__ == "__main__":
    main()