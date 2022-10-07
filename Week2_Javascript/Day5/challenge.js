function Verificateur(nombre) {
		type = Number(nombre);
		if (!type) {
			console.log("Vueillez tapez un nombre");
			return false;
		}else {
			return true;
		}
	}

	function bottleNumber() {
		let nombre;
		do {
			nombre = prompt("On commence à combien de bouteilles ??","99");
		} while (!Verificateur(nombre))
		return nombre;
	}


	function bottleSong() {
		let nombre=bottleNumber();
		console.log("We start the song at",nombre,"bottles")
		nombre= nombre-1;
		console.log("Take 1 down, pass it around");
		console.log("we have now" , nombre , "bottles");
		for ( let i = 2; i < nombre; i++) {
			console.log("Take " + i + " down, pass them around");
			console.log("we have now" , nombre-i , "bottles");
			nombre = nombre-i;
		}
		console.log("Take " + nombre + " down, pass them around");
		console.log("we have now 0 bottle");
	}

	bottleSong();