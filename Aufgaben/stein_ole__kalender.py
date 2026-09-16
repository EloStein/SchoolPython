def ist_schaltjahr(jahr):
    if ((jahr % 4 == 0 and jahr % 100 != 0) or jahr % 400 == 0):
        return True
    else:
        return False


def jahreslaenge(jahr):
    if(ist_schaltjahr(jahr)):
        return 366
    else:
        return 365


def monatslaenge(jahr, monat):
    match monat:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            if ist_schaltjahr(jahr):
                return 29
            else:
                return 28

def existiert(jahr, monat, tag):
    if  monat <= 12 and monatslaenge(jahr, monat) >= tag:
        return True
    return False


#print(statement("2 == 2", True, False))
print(jahreslaenge(2001))

