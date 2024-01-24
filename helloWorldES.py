# some fancy decoration

def printbox(word):
    print("**{}**".format(len(word) * "*"))
    print ("*", word , "*")
    print("**{}**".format(len(word) * "*"))

# you want to get into the club? - let's see frist if you're old enough!

print("Wie alt bist du?")

alter = float(input())

print("Du bist also", alter, "Jahre alt.")
print("Bist du dir sicher?")
antwort = input()

while antwort != "ja":
    print("Wie alt bist du denn wirklich?")
    alter = float(input())
    print("Du bist also", alter, "Jahre alt.")
    print("Bist du dir sicher?")
    antwort = input()
    
if alter < 18:
    printbox("Tut mir leid, du darfst hier noch nicht rein!")
else:
    printbox("Komm herein! Ich wünsche dir viel Spaß!")
