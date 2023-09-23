CODES = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digits_lst = [*digits]
        if len(digits_lst) == 0:
            return ""
        if len(digits_lst) == 1:
            return CODES[digits_lst[0]]
        else:
            res = []
            first_numb = digits_lst.pop(0)
            digits = "".join(digits_lst)
            for ele in CODES[first_numb]:
                for next in Solution.letterCombinations(self, digits):
                    temp = ele + next
                    res.append(temp)

            return res