//Exercise1
let sentence = ["my","favorite","color","is","blue"];
console.log(sentence);


//Exercise2
let str1 = "mix";
let str2 = "pod";

let s1=str1.split("");
let s2=str2.split("");
s1.splice(0,2,"i","m");
console.log(s1);
s2.splice(0,2,"o","p");
console.log(s2);

let sum=str1+" "str2;
console.log(sum);


//Exercise3
let num1=Number(prompt("entrer un nombre"));
let num2=Number(prompt("entrer un deuxième nombre"));
alert(num1+num2);