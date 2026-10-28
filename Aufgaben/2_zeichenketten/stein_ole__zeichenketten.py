# Aufgabe 1
def zaehleA(text: str):
    return zaehle(text, "a")

# Aufgabe 2
def zaehle(text: str, buchstabe):
    text = text.lower()
    sum = 0
    for l in text:
        if l == buchstabe:
            sum += 1
    return sum

# Aufgabe 3
def zaehleVokale(text: str):
    vokale = ("a", "e", "i", "o", "u")
    text = text.lower()
    sum = 0
    for i in text:
        for v in vokale:
            if i == v:
                sum += 1
    return sum

# Aufgabe 4
def entferneLeerzeichen(text: str):
    return text.replace(" ", "_")

# Aufgabe 5
def stretch(text: str):
    stretchedText = ""
    for l in text:
        if l == " ":
            stretchedText += "_"
        else:
            stretchedText += l + "_"
    return stretchedText[0:-1]

# Aufgabe 6
def vertausche(text: str):
    neuText = ""
    for l in text:
        if l.islower():
            neuText += l.capitalize()
        else:
            neuText += l.lower()
    return neuText

# Aufgabe 6.1
def vertauscheKompakt(text: str):
    return text.swapcase()

# Aufgabe 7
def aufAb(text):
    text = text.lower()
    neuText = ""
    for i, l in enumerate(text, 1):
        if i % 2:
            neuText += l.upper()
        else:
            neuText += l
    return neuText

# Aufgabe 8
def aufAbAnzahl(text , n):
    neuText = ""
    for i, l in enumerate(text, 1):
        if i % n == 0:
            neuText += l.upper()
        else:
            neuText += l.lower()
    return neuText

# Aufgabe 9
def verschiebe(text):
    n = 3
    neuText = ""
    for l in text:
        if ord(l) + n <= 90:
            neuText += chr(ord(l)+n)
        else:
            neuText += chr(ord(l)+n -26)
    return neuText

# Aufgabe 9.1
def verschiebe2(text, vbs):
    n = ord(vbs) - 65
    neuText = ""
    for l in text:
        if ord(l) + n <= 90:
            neuText += chr(ord(l)+n)
        else:
            neuText += chr(ord(l)+n -26)
    return neuText




