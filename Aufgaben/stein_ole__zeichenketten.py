def zaehle_a(text: str):
    return zaehle(text, "a")

## Aufgabe 2
def zaehle(text: str, buchstabe):
    sum = 0;
    for i in text:
        if i == buchstabe:
            sum = sum + 1
    return sum

## Aufgabe 3
def zaehle_vokale(text: str):
    vokale = ("a", "e", "i", "o", "u")
    text = text.lower()
    sum = 0;
    for i in text:
        for v in vokale:
            if i == v:
                sum = sum + 1
    return sum

## Aufgabe 4
def entferneLeerzeichen(text: str):
    return text.replace(" ", "_")

## Aufgabe 5
def stretch(text: str):
    stretchedText = ""
    for l in text:
        if l == " ":
            stretchedText += "_"
        else:
            stretchedText += l + "_"
    return stretchedText[0:-1]

## Aufgabe 6
def vertausche(text: str):
    neuText = ""
    for l in text:
        if l.islower():
            neuText += l.capitalize()
        else:
            neuText += l.lower()
    return neuText

def vertauscheKompakt(text: str):
    return text.swapcase()


## Aufgabe 7
def aufAb(text):
    newString = ""
    i = 0;
    for l in text:
        if i % 2 == 0:
            newString = newString + l.upper()
        else:
            newString = newString + l.lower()
        i = i + 1
    return newString

## Aufgabe 7 v2
def aufAbV2(text):
    neuText = text.lower()
    i = 0
    for l in text:
        if i % 2 == 0:
            neuText = changeOnIndex(neuText, i, l.upper())
        i = i + 1
    return neuText


def changeOnIndex(text, index, change):
    return text[0:index] + change + text[index+1:]


## Aufgabe 8
def aufAbAnzahl(text , n):
    neuText = ""
    i = 1;
    for l in text:
        if i < n:
            neuText += l.lower()
        else:
            i = 0
            neuText += l.upper()
        i += 1
    return neuText

# Überladene aufAb Funktion für mer Optionen
def aufAbAnzahl(text , n, shouldBeCapitalized):
    neuText = ""
    for i, l in enumerate(text, 0):
        if i % n == 0 and allowCapatalizedStart(shouldBeCapitalized, i):
            neuText += l.upper()
        else:
            neuText += l.lower()
    return neuText

def allowCapatalizedStart(s, i):
    if not s:
        if i == 0:
            return False
    return True

# Aufgabe 9
## Kommt saaave noch

print(aufAbAnzahl("aaabbbccc",3, True))


