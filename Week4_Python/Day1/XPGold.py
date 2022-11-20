#Exercise1

print((("Hello world\n")*4) + (("I love python\n")*4))



#Exercise2
mois=int(input("saisissez un mois à partir de son numero (exemple: Janvier = 1)\n"))
if 1 <= mois <= 12:
	if 3 <= mois <= 5:
		print("on est au printemps")
	elif 6 <= mois <= 8:
		print("c'est l'été")
	elif 9 <= mois <= 11:
		print("Nous sommes en Automne")
	else:
		print("c'est l'hiver!!!")
else:
	print("choisissez un bon numero")


