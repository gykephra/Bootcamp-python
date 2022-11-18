//Exercise1
5 >= 1 //True
0 === 1 //False
4 <= 1 //False
1 != 1 // False
"A" > "B" //False
"B" < "C" //True
"a" > "A" //True
"b" < "A" //false
true === false //False
true != true //False


//Exercise2
let numbs = prompt("Tapez deux nombres séparés par une virgule");
numbs = numbs.split(",");
console.log("La somme de" , numbs[0] , " et " , numbs[1] , " est " , Number(numbs[0]) + Number(numbs[1]) );

//Exercise3 
let sentence = prompt("Saisir une phrase qui contient le mot Nemo");
console.log(sentence);
sentence=sentence.split(" ");
word = sentence.indexOf("Nemo");

console.log("Chaine trouvée à la position" , word);

    if (word != -1) {
        console.log("Chaine trouvée à la position" , word);  
    } else {
        console.log("La chaine n'a pas été trouvé");  
    }

//Exercise4: 
let numb = Number(prompt("Tapez un nombre:"));
let firstLett = "b";
    if (numb < 2) {
        firstLett = "boum";
        if ((numb%2) == 0){
            console.log("divisible par 2" , firstLett + "!");
        } else if ((numb%5) == 0){
            console.log("divisible par 5" , firstLett.toUpperCase() + "!");
        } else if ((numb%5) && (numb%2) == 0){
            console.log(firstLett.toUpperCase() + "!");
        } else {
            console.log("Ni divisible par 2, ni par 5  ", firstLett);
        }
    } else {
        for (let i = 1; i <= numb ; i++) {
            firstLett=firstLett+"o";
        }
        firstLett=firstLett+"u";
        firstLett=firstLett+"m";
        if ((numb%2) == 0){
            console.log("divisible par 2" , firstLett + "!");
        } else if ((numb%5) == 0){
            console.log("divisible par 5" , firstLett.toUpperCase() + "!");
        } else if ((numb%5) && (numb%2) == 0){
            console.log(firstLett.toUpperCase() + "!");
        } else {
            console.log("Ni divisible par 2, ni par 5  ", firstLett);
        }
    } 