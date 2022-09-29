/*Exercise1*/
let people = ["Greg", "Mary", "Devon", "James"];
people.shift();
people.splice(3, 1, "Jason");
people.push("Ephraîm");
console.log(indexOf("Mary"))
console.log(people.slice(1,3))
people.indexOf("Foo")//-1 because Foo doesn't in people
let last = people[people.length -1]

/*Partie II*/
for (let name=0; name<people.length; name++) {
	console.log(people[name])
}

for (let name=0; name<people.length; name++) {
	if(name==="Jason"){
		break;
	}
	console.log(people[name])
}


/*Exercise2*/
let colors = ["Blue", "White", "Black", "Red", "Green"]
for (let color=0; color<colors.length; color++) {
	console.log("My "+colors.indexOf(color)+" choice is ", colors[color])
}

let colors = ["Blue", "White", "Black", "Red", "Green"]
//let choices = ["1st", "2nd", "3rd", "4th", "5th"]
for (let color=0; color<colors.length; color++)
//for (let choice = 0, choice<choices.lenth; choice++)
{
	console.log("My "+choices[choice]+" choice is ", colors[color])
}
