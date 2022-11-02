/**
 * @param {number} num
 * @return {string}
 */


var intToRoman = function(num) {
    let numbers = {
    1000:"M",
    900:"CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
  }
  let numeric = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
  if(numbers.hasOwnProperty(num)) {
      return numbers[num];
  }
  let div = 0
  let nb
  let rest = num
  let roman = ""
  while(rest > 0) {
    
    if(numbers.hasOwnProperty(rest)) {
      roman += numbers[rest]
      return roman
    }
    
    let pos = findPos(numeric, rest);

    nb = rest - (rest % numeric[pos]);
    //console.log(nb)
    div = nb / numeric[pos]; 
    //console.log(div)
    rest = rest % numeric[pos];
    roman = concatRoman(roman, numbers[numeric[pos]], div);
    
    
  }
  
  return roman;
};


function findPos(arr, val) {
  for(let i in arr) {
    if(val > arr[i]) {
      return i;
    }
  }
  return -1;
};

function concatRoman(str, sym, times) {

  for(let i = 0; i < times; i++) {
    str += sym
  }
  return str
};
