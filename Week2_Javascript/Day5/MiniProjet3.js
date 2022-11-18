	function longueurmot(word) {
		if (word.length < 8)
			return false;
		else
			return true;
	}

	function saisieDuMot(){
		let word;
		do{
			word = prompt("Tapez un mot d'au moins 8 lettres"); 
		} while (!longueurmot(word))
		return word;
	}



	function conditLettre(lettre) {
		if (lettre.length != 1)
			return false;
		else
			return true;
	}

	function LettreAentrer() {
		let lettre;
		do {
			lettre = prompt("Tapez une lettre");
		} while(!conditLettre(lettre))
		return lettre;
	}

function check(word,word1,lettre) {
		let word2 = "";
		for(let x = 0; x < word.length; x++){
			if ( word[x] == lettre && lettre != word1[x]) {
				word2 += word[x];
			} else {
				word2 += word1[x];
			}
		}
		return word2;
	


function HangMan() {
		let word = saisieDuMot();
		let word1 = "*".repeat(word.length);
		console.log(word1);
		let chance = 0;
		do {
			let lettre = LettreAentrer();
			let word2 = check(word,word1,lettre);
			
			if (word1 == word) {
				console.log("CONGRATS YOU WIN")
				return;
			}
			if (chance == 10)
				console.log("YOU LOSE.");
		} while( chance < 10)
	}

	HangMan();