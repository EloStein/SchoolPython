# Ignorieren sie die korzen Funktionen
def istSchaltjahr(jahr):
    return statement(f"({jahr} % 4 == 0 and {jahr} % 100 != 0) or {jahr} % 400 == 0", True, False)


def jahreslaenge(jahr):
    return statement(f"(istSchaltjahr({jahr}))", 366, 365)


def monatslaenge(jahr, monat):
    match monat:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12: return 31
        case 4 | 6 | 9 | 11: return 30
        case 2: return statement(f"istSchaltjahr({jahr})", 29, 28)
    return "Fehler bei Eingabe: jahr-> " + str(jahr) + " monat->" + str(monat)


def existiert(jahr, monat, tag):
    return statement(f"{monat} <= 12 and monatslaenge({jahr}, {monat}) >= {tag}", True, False)

def statement(statement, true, false):
    if bool(eval(statement)):
        return true
    else:
        return false

def switch(statement, true, false):
    if eval(statement):
          return true
    else:
        return false


#print(statement("2 == 2", True, False))
print(monatslaenge(2000,3))
print(existiert(2000,2,29))

