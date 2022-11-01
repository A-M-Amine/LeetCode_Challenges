class Solution:
    def isValid(self, s: str) -> bool:

        validDict = { "(": ")", "{": "}", "[":"]"}
        pile = []
        pile2 = []

        if len(s) == 1: 
            return False

        for char in [*s]:
            if(char in validDict):
                pile.append(char)
            else:
                pile2.append(char)
                if len(pile) > 0:
                    if(validDict[pile[-1]] != char):
                        return False
                    pile.pop()
                    pile2.pop()
        
        if len(pile) == 0 and len(pile2) == 0:
            return True
        else:
            return False

                                
                    