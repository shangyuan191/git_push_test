import random
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabetc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def draw():
    random.shuffle(alphabet)
    g=alphabet.pop(0)
    return g
al=input("Guess the lower case alphabet: ")
list=[["a-d: "],["e-h: "],["i-l: "],["m-p: "],["q-t: "],["u-x: "],["y-z: "]]
if alphabetc.index(al)<4:
    list[0].append("*")
if alphabetc.index(al)<8 and 3<alphabetc.index(al):
    list[1].append("*")
if alphabetc.index(al)<12 and 7<alphabetc.index(al):
    list[2].append("*")
if alphabetc.index(al)<16 and 11<alphabetc.index(al):
    list[3].append("*")
if alphabetc.index(al)<20 and 15<alphabetc.index(al):
    list[4].append("*")
if alphabetc.index(al)<24 and 19<alphabetc.index(al):
    list[5].append("*")
if alphabetc.index(al)<26 and 23<alphabetc.index(al):
    list[6].append("*")
gu=draw()
i=1
while True:
    if al in alphabetc:
        if al==gu:
            print("Congratulations!You guessed the alphabet","'",gu,"'","in",str(i),"tries")
            break
        else:
            if alphabetc.index(gu)< alphabetc.index(al):
                print("The alphabet you are looking for is alphabetically lower.")
                al=input("Guess the lower case alphabet: ")
                i=i+1
                if alphabetc.index(al)<4:
                    list[0].append("*")
                if alphabetc.index(al)<8 and 3<alphabetc.index(al):
                    list[1].append("*")
                if alphabetc.index(al)<12 and 7<alphabetc.index(al):
                    list[2].append("*")
                if alphabetc.index(al)<16 and 11<alphabetc.index(al):
                    list[3].append("*")
                if alphabetc.index(al)<20 and 15<alphabetc.index(al):
                    list[4].append("*")
                if alphabetc.index(al)<24 and 19<alphabetc.index(al):
                    list[5].append("*")
                if alphabetc.index(al)<26 and 23<alphabetc.index(al):
                    list[6].append("*")
            else:
                print("The alphabet you are looking for is alphabetically higher.")
                al=input("Guess the lower case alphabet: ")
                i=i+1
                if alphabetc.index(al)<4:
                    list[0].append("*")
                if alphabetc.index(al)<8 and 3<alphabetc.index(al):
                    list[1].append("*")
                if alphabetc.index(al)<12 and 7<alphabetc.index(al):
                    list[2].append("*")
                if alphabetc.index(al)<16 and 11<alphabetc.index(al):
                    list[3].append("*")
                if alphabetc.index(al)<20 and 15<alphabetc.index(al):
                    list[4].append("*")
                if alphabetc.index(al)<24 and 19<alphabetc.index(al):
                    list[5].append("*")
                if alphabetc.index(al)<26 and 23<alphabetc.index(al):
                    list[6].append("*")
    else:
        print("Please enter a lower case alphbet.")
        al=input("Guess the lower case alphabet: ")
print("Guess Histgram:")
for row in list:
    print("".join(row))
