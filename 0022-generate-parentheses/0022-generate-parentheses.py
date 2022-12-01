class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        outcomes = {"()"}


        if n == 1:
            return list(outcomes)

        for k in range(1, n):

            res = set()

            for j in outcomes:

                for i in range(k + 1):

                    combo = insert(j, i, "()")

                    res.add(combo)

            outcomes = res


        return outcomes






def insert(text, pos, obj):

    if int(len(text) / 2) == pos or pos < len(text):
        text = text[:pos] + obj + text[pos:]
        return text
    
    text = text + obj
    return text