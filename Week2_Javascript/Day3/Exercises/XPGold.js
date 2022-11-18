//Exercise1 
	let numbers = [123, 8409, 100053, 333333333, 7]
	for (numb of numbers) {
		if (numb%3 == 0) 
			console.log(numb ,": true");
		else 
			console.log(numb ,": fasle");
	}

//Exercise2 
	let guestList = {
		randy: "Germany",
		karla: "France",
		wendy: "Japan",
		norman: "England",
		sam: "Argentina"
	}
	
	nom = prompt("Saisissez votre nom");
	
	if (nom in guestList)
		console.log("Hi! I'm" , nom + ", and I'm from ",guestList[nom]);	
	else
		console.log("Hi! I'm a guest.");

//Exercise3
	let age = [20,5,12,43,98,55];
	let somme = 0;

	for(j of age)
		somme += j;
	console.log("La somme de tous les nombres:",somme)
	
	let ageElevé = 0;
	for (j of age)
		if (j > ageElevé)
			ageElevé = j;
	console.log("L'âge le plus élevé :",ageElevé,"ans");