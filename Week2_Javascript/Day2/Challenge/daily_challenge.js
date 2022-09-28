let sentence = "My bootcamp going well, it's not bad"
let wordNot = sentence.indexOf('not')
let wordBad = sentence.indexOf('bad')

if((wordNot =! -1) || (wordBad =! -1)) {
	console.log("My bootcamp going well, it's good")
}
else
	console.log(sentence)
