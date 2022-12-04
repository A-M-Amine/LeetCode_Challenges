class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        seperators = checkPile(s)
        cond = seperate(s,seperators)


        if len(cond) > 0:

            mx = 0
            for ele in cond:
                mx = max(len(ele),mx)

            return mx

        return 0
    

def checkPile(s):


    pile = []
    

    res = []
    for i in range(len(s)):
        if pile:
            if pile[-1][0] == "(" and s[i] == ")":
                pile.pop()
            else:
                pile.append((s[i],i))
        else:
            pile.append((s[i],i))

    return pile


def seperate(s, lst):

    res = []
    seperators = [j for i, j in lst]

    tmp = ""
    for i in range(len(s)):

        if not i in seperators:
            tmp += s[i]
        else:
            if tmp != "":
                res.append(tmp)
                tmp = ""
    
    if tmp != "":
        res.append(tmp)

    return res

