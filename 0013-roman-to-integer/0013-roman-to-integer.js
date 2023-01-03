/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
 
    // Create an array of symbols from the input string
    s = [...s];

    // Create an object of symbol values
    const sym = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };

    // Initialize nb to 0 and mem to the value of the first symbol
    let nb = 0;
    let mem = sym[s[0]];

    // Iterate through the symbols
    for (const i of s) {
      // Check if the current symbol has a greater value than mem
      if (sym[i] > mem) {
        // If it does, add the value of the symbol minus twice the value of mem to nb
        nb = nb + (sym[i] - 2 * mem);
      } else {
        // If it doesn't, simply add the value of the symbol to nb and update mem
        nb += sym[i];
        mem = sym[i];
      }
    }

    // Return the integer value of nb
    return nb;
  
};