/*Exercise1*/
let x = 10;
let y = 5;

if (x>y) {
	console.log("x is the biggest number");
}

/*Exercise2*/
let newDog = "Chihuahua";
newDog.length;
newDog.toUpperCase();
newDog.toLowerCase();

if (newDog == "Chihuahua") {
	console.log("J'adore les chihuahuas, c'est ma race de chien préférée")
} else
console.log("Je m'en fous je prefère les chats")

/*Exercise3*/
let nbr = prompt('Entrez un nombre:',);
if((nbr%2)==0){
	alert(`${nbr} est un nombre pair`);
} else 
alert(`${nbr} est un nombre impair`);

/*Exercise4*/
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
if(users.length==0){
	console.log("personne n'est en ligne")
}else if (users.length==1) {
	console.log(users[0] est en ligne)
}else if (users.length==2) {
	console.log(users[0] +"et" users[1] sont en ligne)
}else
	console.log(users[0] + "," users[1] + "2 autres sont en ligne")