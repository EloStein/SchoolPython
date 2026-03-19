# Hilfsmethoden
def containsJa(value):
    if "ja" in value.lower():
        return True
    else:
        return False

# Nummer A1
def checkFive():
    number = int(input())
    if number == 5:
        print("Input hat den Wert 5")
    else:
        print("Input hat nicht den Wert 5")

# Nummer A2
def inRange():
    rangeStart = float(input("Gib den Anfang des Zahlenraums ein"))
    rangeEnd = float(input("Gib den Anfang des Zahlenraums ein"))
    number = float(input("Gib deine Zahl ein"))
    if rangeEnd >= number >= rangeStart:
       print("Input Number in Range enthalten")
    else:
        print("Input Number nicht in Range enthalten")

# Nummer B
def sugarOrMilk():
    milk = str(input("Willst du Milch in den Kaffee? [Ja/Nein]"))
    sugar = str(input("Willst du Zucker in den Kaffee? [Ja/Nein]"))

    if containsJa(milk):
        if containsJa(sugar):
            print("Kaffee mit Milch und Zucker, immer gern")
        else:
            print("Kaffee mit Milch kommt sofort")
    else:
        if containsJa(sugar):
            print("Ok Kaffee nur mit Zucker kommt sofort ")
        else:
            print("Ok du magst ihn Schwarz, warum nicht")

# Nummer C1
def whatIsIt():
    alive = input("Lebt es?")
    if containsJa(alive):
        carnivore = input("Frisst es Fleisch?")
        if containsJa(carnivore):
            print("Es ist ein Tiger")
        else:
            print("Es ist ein Esel")
    else:
        drivable = input("Kann es fahren?")
        if containsJa(drivable):
            print("Es ist ein Auto")
        else:
            edible = input("Kann man es essen?")
            if containsJa(edible):
                print("Es ist Gemüse")
            else:
                print("Es ist der Boden")

# Nummer C2
def favoriteDrink():
    answer = input("Saft oder Softdrink?")
    if answer == "Saft":
        answer = input("Apfelsaft, O-Saft? oder Traubensaft")
        if answer == "Apfelsaft":
            print("Gute Wahl, Äpfel sind lecker")
        elif answer == "O-Saft":
            print("O-Saft, Vitamin pur!")
        else:
            print("Trauben, beste Wahl!")
    elif answer == "Softdrink":
        answer = input("Cola, Fanta oder Sprite")
        if answer == "Cola":
            print("The Original Taste!")
        elif answer == "Fanta":
            print("Mhh Fanta...")
        else:
            print("Sprite, mein Favorite!")
    else:
        print("Abwarten und Tee trinken...")

