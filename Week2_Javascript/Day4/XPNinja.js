//Exercise1 
function getRandom(max) {
  return Math.floor(Math.random() * max);
}

let nombre = getRandom(101);

for ( let i = 1 ; i <= nombre; i++)
{ 
	if (i%2 == 0 )
	{ 
	    console.log(i);
	}
}

//Exercise2
function capitalize (chaine) 
{
let chainePair = "";
let chaineImpair = "";
for ( let i = 0; i < chaine.length; i++)
	if (i%2 == 0)
		chainePair += chaine[i].toUpperCase();
	else
		chainePair += chaine[i];
	

for ( let i = 0; i < chaine.length; i++)
	if (i%2 != 0)
		chaineImpair += chaine[i].toUpperCase();
	else
		chaineImpair += chaine[i];

		console.log(chainePair,chaineImpair);

capitalize ("abcdef");

//Exercise3 
	function palindrome(mot) {
		mot=mot.toLowerCase();
		if (mot.length%2 == 0)
			return false;
		else
			for(let i = 0; i < mot.length; i++)
				if (mot[i] != mot[mot.length-i-1])
						return false;
		return true;
	}

	palindrome("Madam");

//Exercise4 
	function biggestNumberInArray(NumbArr) {
		let biggestNumber = 0;
		if (NumbArr == [])
			return 0;
		for (x of NumbArr)
			if (Number(x) && x > biggestNumber)
				biggestNumber = x;
		return biggestNumber;
	}

	biggestNumberInArray([-1,0,3,100, 99, 2, 99]);

//Exercice 5 
	function NoOccur(item) {
		let item1 = [];
		for (i of item){
			let valide = 0;
			for (j of item1)
				if (item1 == [])
					item1[0]=i;
				else if (i == j)
					valide = 1;
			if (valide==0)
				item1[item1.length]=i;
		}
		return item1;
	}

	NoOccur([1,2,3,3,3,3,4,5]);