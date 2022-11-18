//Exercise 1 
//Partie 1
	function Verificateur(nombre) {
		type = Number(nombre);
		if (!type) {
			console.log("Veuillez tapez un nombre");
			return false;
		} else if (nombre < 0 && nombre > 10){
			console.log("Mauvais choix!!!");
			return false;
		} else {
			return true;
		}
	}

	function aléatoireNum(min,max) {
		min = Math.ceil(min);
		max = Math.floor(max+1);
		let nombre = Math.floor(Math.random()* (max - min)) + min;
		return nombre;
	}

	function playTheGame() {
		let confirmation=confirm("Une partie de jeu???")
		if (!confirmation) {
			console.log("Bye alors !!!");
			return;
		} else {
			let userNumber;
			do {
				userNumber = prompt("Tapez un nombre entre 0 et 10");
				if (Verificateur(userNumber)) {
					computerNumber = aléatoireNum(0,10);
					Comparateur(userNumber,computerNumber);
				}
			} while (!Verificateur(userNumber))
		}

	}

	//Partie 2
	function Comparateur(userNumber,computerNumber) {
		let i=0;
		while(i!=4) {
			if (userNumber == computerNumber) {
				alert("VOUS AVEZ GAGNE!!!");
				return;
			} else if (userNumber > computerNumber && i!=3) {
				userNumber = prompt("Trop grand , devine encore"); 
				while(!Verificateur(userNumber))
					userNumber = prompt("Entrez un nombre entre 0 et 10");
			}
			else if (userNumber < computerNumber && i!=3) {
				userNumber = prompt("Trop petit , devine encore"); 
				while(!Verificateur(userNumber))
					userNumber = prompt("Entrez un nombre entre 0 et 10");
			}	
			else if ( i == 3) {
				alert("pas de bol");
				return;
			}
			i++;
		}
	}