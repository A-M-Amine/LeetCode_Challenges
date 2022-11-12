/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    
    memo = [0,1,2];
    
    for(i = 3; i<n + 1; i++) {
        memo[i] = memo[i-1] + memo[i-2];
    }
    
    return memo[n]
    
};

