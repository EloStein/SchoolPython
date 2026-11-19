def b2z(buchstabe):
	return ord(buchstabe) - 65

def z2b(zahl):
	return chr(zahl + 65)

datei = open("geheim.txt")
inhalt = datei.read()

anzahlen = []
for i in range(26):
	anzahlen.append(0)

for b in inhalt:
	if b != " ":
		i = b2z(b)
		anzahlen[i] = anzahlen[i] + 1

for i in range(len(anzahlen)):
	print(z2b(i), anzahlen[i])
