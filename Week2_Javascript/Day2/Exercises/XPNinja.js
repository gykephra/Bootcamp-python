//Exercise1
let an1= Number(prompt("Tapez la première année de naissance"));

let an2=Number(prompt("Tapez la deuxieme année de naissance"));

if (an1<an2){
	console.log((2*an2)-(an1));
}
if (an2<an1) {
	console.log((2*an1)-(an2));

}

//Exercise2
let code = Number(prompt("Saisissez votre code postal");

if(code.length == 5)
{
	console.log("succes");
}
else {console.log("erreur");}

//Exercise3
let motSecret = prompt("Saisissez votre mot");

let motSecret1 = motSecret.replace(/[a,u,o,e,i]+/g,"");
console.log(motSecret1);
