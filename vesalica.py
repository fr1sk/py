import random
import os

def vesalica(x):
    i = 0
    j=0
    temp = []
    br = 5
    br1 = len(x)
    while 1:
        #print("\n"*20)
        if br == 5:
            print(" |---\ ")
            print(" O   |")
            print('/|\  |')
            print("/ \  |")
            print("     |")
            print("======")
            print("\n"*2)
        elif br == 4:
            print(" |---\ ")
            print(" O   |")
            print('/|   |')
            print("/ \  |")
            print("     |")
            print("======")
            print("\n"*2)
        elif br == 3:
            print(" |---\ ")
            print(" O   |")
            print('/|   |')
            print("  \  |")
            print("     |")
            print("======")
            print("\n"*2)
        elif br == 2:
            print(" |---\ ")
            print(" O   |")
            print('/|   |')
            print("     |")
            print("     |")
            print("======")
            print("\n"*2)
        elif br == 1:
            print(" |---\ ")
            print(" O   |")
            print(' |   |')
            print("     |")
            print("     |")
            print("======")
            print("\n"*2)
        else:
            print(" |---\ ")
            print(" X   |")
            print('/|\  |')
            print("/ \  |")
            print("     |")
            print("======")
            print("\n"*2)
            print("izgubili ste")
            exit(1)

        if br >= 0 and br1 != 0:
            for i in range (len(x)):
                temp.append("_")
                print(temp[i], end='')
                print(" ",end='')
            print("\n"*3)
            print("preostalo " + repr(br) + " pokusaja")
            slovo = input("pogodi slovo: ")

            if slovo in x:
                print("\n"*20)
                for indeks, sur in enumerate(x):
                    if sur == slovo:
                        br1=br1-1
                        temp[indeks] = slovo;
            else:
                print("\n"*20)
                print("rec ne sadrzi slovo: "+slovo)
                print("\n"*3)
                br=br-1
        elif br == 0:
            print("izgubili ste")
            exit(1)
        elif br1 == 0:
            print("pobedili ste")
            #print("pronasli ste rec " +x+" u " +repr(len(x)-br)+" pokusaja")
            exit(1)


reci = ["papagaj", "svinja", "paradajz", "zgitk", "padre", "sat", "motor", "geek", "cvece", "kavurma", "cvarci"]
rec = random.randrange(0, len(reci))
print(reci[rec])
x = reci[rec]
print("\n"*20)
vesalica(x)
