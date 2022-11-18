//Exercise1
let lang=prompt("Langue?").lowercase

switch(lang) {
  case francais:
    console.log("Bonjour");
    break;
  case anglais:
    console.log("Hello");
    break;
  case hebreux:
    console.log("Shalom");
    break;
  default:
    console.log("01110011"+" 01101111" +"01110010 " +"01110010 "+" 01111001");  
}


//Exercice2
let note= Number (prompt("Votre note ?"));

if (note>90) {
  console.log("A");
}
else if ((note>80) && (note<=90)) {
  console.log("B");
}
else if ((note>70) && (note<=80)) {
  console.log("C");
}  
else{
  console.log("D");
}



//Exercise3
let verb=prompt("Tapez un verbe").lowercase;
if((verb.length >=3) && (verb.endsWith('ing') is (false)))
{

  console.log(verb.push("ing"));
}


if ((verb.length >=3)&&(verb.endsWith('ing'))){
 console.log(verb.push("ly"))
};
if (verb.length < 3){
  console.log(verb);
}