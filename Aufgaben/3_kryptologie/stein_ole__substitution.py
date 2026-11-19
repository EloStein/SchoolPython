def substitution(klartext: str, gta: str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    geheimtext = ""
    for b in klartext:
        if b == " ":
            geheimtext += b
        else:
            for i, gb in enumerate(alphabet):
                geheimtext += gta[i] if b == gb else ""
    return geheimtext


print(substitution("ABC CBA", "QMJZTGFKPWLSBOXNCRYEVHIADU"))