alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def substitution3(klartext: str, gta: str):
    geheimtext = ""
    for b in klartext:
        geheimtext += " " if b == " " else gta[next((i for i, gb in enumerate(alphabet) if b == gb), None)]
    return geheimtext

def substitution(klartext: str, gta: str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    geheimtext = ""
    for b in klartext:
        if b == " ":
            geheimtext += b
        else:
            for i in range(len(alphabet)):
                if (b == alphabet[i]):
                    geheimtext += gta[i]
    return geheimtext