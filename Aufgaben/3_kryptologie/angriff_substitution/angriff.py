
def substituiere(eingangsalphabet, ausgangsalphabet, buchstabe):
	pos = 0
	for i in range(len(eingangsalphabet)):
		if (buchstabe == eingangsalphabet[i]):
			pos = i
	neuerBuchstabe = ausgangsalphabet[pos]
	return neuerBuchstabe


geheimdatei = open("geheim2.txt", "r")
geheimtext = geheimdatei.read()
geheimdatei.close()

gta = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
kta = "xmCytgfvwchkbpniarleUuWosd"

klartext = ""
for bs in geheimtext:
	if (bs == " "):
		kbs = " "
	else:
		kbs = substituiere(gta, kta, bs)
	klartext = klartext + kbs

klardatei = open("klar.txt", "w")
klardatei.write(klartext)
klardatei.close()
print (klartext)

