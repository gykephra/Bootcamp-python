//Exercise1

function infoAboutMe(){
	console.log("Hey my name is Ephraïm Kokou GBOUGBO-YAO and i'm 22yo");
}

infoAboutMe();



function infoAboutPerson(personName, personAge, personFavoriteColor){
	console.log("Hi your name is "+personName+",you are "+personAge+" year old "+"  and your favorite color is "+personFavoriteColor);

}
infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");




//Exercise2

function calculateTip() {
	let bill =Number(prompt("How much is your bill?"));
	if (bill<50){
		let tip=(20*bill)/100;
	}
	else if ((bill>=50)&&(bill<=200)){
		let tip=(15*bill)/100;
	}
	else{
		let tip=(10*bill)/100;
	}

	console.log("the tip amount is "+tip);
	console.log("the final bill is "+(bill+tip));
};

calculateTip()



//Exercise3

function isDivisible(){
	let totalnumb=0;
	for (let numb=0; numb<=500; numb++) {
		if (numb%23==0) {
			console.log(numb)
			totalnumb=totalnumb+numb;
		}
		
	}
	console.log("Sum:",totalnumb);
}


isDivisible();



//Exercise4


let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList=["banana", "orange", "apple"]; 

function myBill(){
	for (let item in shoppingList) {

		if (shoppingList[item] in stock) {
			console.log(shoppingList[item]);
		}
	}

myBill();