//Exercise1 
	function isBlank(str1) {
		if (str1 == "") return true;
		else return false;
	}

	console.log(isBlank(''));
	console.log(isBlank('abc'));

//Exercise2
	function abrev(str2) {
		str2 = str2.split(" ");
		str2C = str2[0] + " ";
		for (let i = 1; i < str2.length; i++)
			str2C += str2[i][0].toUpperCase() + ". ";
		return str2C;
	}

	console.log(abrev("Robin Singh"));


//Exercise3
	function swapCase (str3) {
		let str3C = "";
		for (let i = 0; i <str3.length;i++)
			if (str3[i] == str3[i].toUpperCase()) 
				str3C += str3[i].toLowerCase();
			else 
				str3C += str3[i].toUpperCase();
		console.log(str3C);
	}

	swapCase('The Quick Brown Fox');

//Exercise4 
function isOmnipresent(tab, numb) {
	for (i of tab) 
		for (j of i)
			if (numb == j) return true;
			else return false;
}

isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1);
isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6);