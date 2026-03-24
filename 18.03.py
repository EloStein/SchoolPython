# Hilfsmethoden
def containsJa(value):
    if "ja" in value.lower():
        return True
    else:
        return False

# Nummer A1
def A1():
    zahl = int(input("Gib eine auf 5 zu prüfende Zahl ein:"))
    if zahl == 5:
        print("Input hat den Wert 5")
    else:
        print("Input hat nicht den Wert 5")

# Nummer A2
def A2():
    anfang = float(input("Gib den Anfang des Zahlenraums ein:"))
    ende = float(input("Gib den Anfang des Zahlenraums ein:"))
    zahl = float(input("Gib deine Zahl ein:"))
    if ende >= zahl >= anfang:
       print("Input Number in Range enthalten")
    else:
        print("Input Number nicht in Range enthalten")

# Nummer B
def B():
    milch = str(input("Willst du Milch in den Kaffee? [Ja/Nein]"))
    zucker = str(input("Willst du Zucker in den Kaffee? [Ja/Nein]"))

    if containsJa(milch):
        if containsJa(zucker):
            print("Kaffee mit Milch und Zucker, immer gern")
        else:
            print("Kaffee mit Milch kommt sofort")
    else:
        if containsJa(zucker):
            print("Ok Kaffee nur mit Zucker kommt sofort ")
        else:
            print("Ok du magst ihn Schwarz, warum nicht")

# Nummer C1
def C1():
    lebend = input("Lebt es?")
    if containsJa(lebend):
        carnivore = input("Frisst es Fleisch?")
        if containsJa(carnivore):
            print("Es ist ein Tiger")
        else:
            print("Es ist ein Esel")
    else:
        fahrbar = input("Kann es fahren?")
        if containsJa(fahrbar):
            print("Es ist ein Auto")
        else:
            essbar = input("Kann man es essen?")
            if containsJa(essbar):
                print("Es ist Gemüse")
            else:
                print("Es ist der Boden")

# Nummer C2
def C2():
    antwort = input("Saft oder Softdrink?")
    if antwort == "Saft":
        antwort = input("Apfelsaft, O-Saft? oder Traubensaft")
        if antwort == "Apfelsaft":
            print("Gute Wahl, Äpfel sind lecker")
        elif antwort == "O-Saft":
            print("O-Saft, Vitamin pur!")
        else:
            print("Trauben, beste Wahl!")
    elif antwort == "Softdrink":
        antwort = input("Cola, Fanta oder Sprite")
        if antwort == "Cola":
            print("The Original Taste!")
        elif antwort == "Fanta":
            print("Mhh Fanta...")
        else:
            print("Sprite, mein Favorite!")
    else:
        print("Abwarten und Tee trinken...")

print("Hallo, um eine Aufgabe abzurufen einfach A1, A2, B, C1, C2 eingeben und 'Enter' drücken")
aufgabe = str(input())
if aufgabe == "A1":
    A1()
elif aufgabe == "A2":
    A2()
elif aufgabe == "B":
    B()
elif aufgabe == "C1":
    C1()
elif aufgabe == "C2":
    C2()
else:
    print("Angefragte Aufgabe nicht gefunden")