class Solution:
    def romanToInt(self, s: str) -> int:
        s = [*s]
        sym = {"I":1,"V":5,"X":10,"L":50,"C":100,"D" :500,"M":1000}

        nb = 0
        mem = sym[s[0]]

        for i in s:
            if sym[i] > mem:   
                nb = nb + (sym[i] - 2 * mem)
            else:
                nb += sym[i]
                mem = sym[i]
                
        return nb

        