#!/usr/bin/python3
def asciiLetters(value) :
    nbr = 0
    nbr2 = 0 
    for i in value :
        print("Lettre : ", i," = ",ord(i))
        nbr += ord(i)
    print(nbr)

    return nbr

def asciiLetters2(value) :
    nbr2 = 0
    for i in value :
        if nbr2 == 0:
            nbr2 = ord(i)
        else :
            print("nbr2 : ", nbr2 + ord(i))
            nbr2 += ord(i) + nbr2
    
    print(nbr2)

    return nbr2

asciiLetters("belone")
print("----------------------------------------------")
asciiLetters2("belone")
