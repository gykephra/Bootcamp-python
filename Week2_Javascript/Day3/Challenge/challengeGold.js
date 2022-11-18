//DECROISSANT
function decroissant(numbers) {
  
  for (let x = 0; x < numbers.length; x++) {
    
    for (let y = x; y < numbers.length; y++) {
      if (numbers[x] < numbers[y]) {
        let tmp = numbers[x]; 
        numbers[x] = numbers[y]; 
        numbers[y] = tmp;
      };
    };
  };
  return numbers;
};
const numbers = [5,0,9,1,7,4,2,6,3,8];
decroissant(numbers);
console.log(numbers);


//CROISSANT
function croissant(numbers) {
  
  var len = numbers.length;       
  var tmp, x, y;                  
  
  for(x = 1; x < len; x++) {
    
    tmp = numbers[x]
    y = x - 1
    while (y >= 0 && numbers[y] > tmp) {
      
      numbers[y+1] = numbers[y]
      y--
    }
    
    numbers[y+1] = tmp
  }
  return numbers
}
const numbers = [5,0,9,1,7,4,2,6,3,8];
croissant(numbers);
console.log(numbers);

