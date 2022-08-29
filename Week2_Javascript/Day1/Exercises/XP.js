/*Exercise1*/
let favfood = "cake";
let favmeal = "breakfast";
console.log(`I eat ${favfood} at every ${favmeal}`);

/*Exercise2*/
let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length;
let myWatchedSeriesString =myWatchedSeries.toString();
console.log(`${myWatchedSeriesSentence} : ${myWatchedSeriesString}`);

/*Exercise3*/
myWatchedSeries.splice(2, 1, "friends");
myWatchedSeries.push("teen wolf");
console.log(myWatchedSeries.unshift("vampires diaries"));
myWatchedSeries.splice(1,1);
console.log();
console.log(myWatchedSeries);

/*Exercise3*/
let celstemp = 37;
let fahrtemp = `${celstemp}`*9/5;

/*Exercise4*/
let c;
let a = 34;
let b = 21;

console.log(a+b)// first expression
//55 because a and b are numbers
//55

a=2

console.log(a+b)//second expression
//23 a still be a number
//23

//c = undefined

console.log(3 + 4 + '5');
//undefined '5' is a constant and 3 and 4 are numbers


/*Exercise5*/
typeof(15);
// Prediction:number
// Actual:number

typeof(5.5);
// Prediction:float
// Actual:number

typeof(NaN);
// Prediction:undefined
// Actual:number

typeof("hello");
// Prediction:string
// Actual:string

typeof(true);
// Prediction:bool
// Actual:boolean

typeof(1 != 2);
// Prediction:boolean
// Actual:boolean

"hamburger" + "s";
// Prediction:hamburgers
// Actual:hambergurs

"hamburgers" - "s";
// Prediction:hamburger
// Actual:NaN

"1" + "3";
// Prediction:13
// Actual:13

"1" - "3";
// Prediction:NaN
// Actual:-2

"johnny" + 5;
// Prediction:johnny5
// Actual:johnny5

"johnny" - 5;
// Prediction:NaN
// Actual:NaN

99 * "hello";
// Prediction:NaN
// Actual:NaN

1 != 1;
// Prediction:boolean
// Actual:false

1 == "1";
// Prediction:false
// Actual:false

1 === "1";
// Prediction:false
// Actual:false
1 == "1"
// Prediction:
// Actual:

/*Exercise6*/
5 + "34";
// Prediction:534
// Actual:534

5 - "4";
// Prediction:1
// Actual:1

10 % 5;
// Prediction:0
// Actual:0

5 % 10;
// Prediction:5
// Actual:5

"Java" + "Script";
// Prediction:JavaScript
// Actual:JavaScript

" " + " ";
// Prediction:double space
// Actual:double space

" " + 0;
// Prediction: 0
// Actual: 0

true + true;
// Prediction:NaN
// Actual:2

true + false;
// Prediction:1
// Actual:1

false + true;
// Prediction:1
// Actual:1

false - true;
// Prediction:-1
// Actual:-1

!true;
// Prediction:false
// Actual:false

3 - 4;
// Prediction:-1
// Actual:-1

"Bob" - "bill";
// Prediction:NaN
// Actual:NaN