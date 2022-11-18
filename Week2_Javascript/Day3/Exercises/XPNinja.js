//Exercise1 
	let pers = [
		{
			nom : "YAO",
			prenom : "Ephra",
			masse : 70,
			taille : 190,
			imc : function () {
				return this.masse/(this.taille*this.taille);
			}
		},
		{
			nom : "Lingani",
			prenom : "Rachid",
			masse : 80,
			taille : 180,
			imc : function () {
				return this.masse/(this.taille*this.taille);
			}
		}
	];
	
	function ImcCompare(){
		if (pers[0].imc() > pers[1].imc())
			console.log(pers[0].nom, pers[0].prenom , "a l'IMC le plus élevé");
		else
			console.log(pers[1].nom , pers[1].prenom  , "a l'IMC le plus élevé");
	}

	ImcCompare();

//Exercise2 
	
	function findAvg(gradesList) {
		moyenne = 0;
		for(x of gradesList)
			moyenne += x;
		moyenne = moyenne / gradesList.length
		if (moyenne > 65)
			console.log("Votre moyenne est :",moyenne + ", vous avez réussi.");
		else 
			console.log("Vous avez échouez, try again");		
	}
	findAvg([42,90,86,99,85]);
	
	