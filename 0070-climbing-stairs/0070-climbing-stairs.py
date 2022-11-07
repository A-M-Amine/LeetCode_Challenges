class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n):
            if n in bank:
                return bank[n]
            else:
                bank[n] = climb(n-1) + climb(n-2)
                return bank[n]
        bank = {1:1, 2:2}
        return climb(n)