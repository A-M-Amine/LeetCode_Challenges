class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        frequency = {}
        pos = 0
        prefix = ""
        if len(strs) == 1:
            return strs[0]        
        
        while strs:

            for word in strs:
                if len(word) > 0 and pos < len(word):
                    letter = word[pos]
                    frequency[letter] = frequency.get(letter, 0) + 1

            max = ("", 0)
            for key, val in frequency.items():
                if val > max[1]:
                    max = (key, val)

            if max[1] <= 1:
                break
            
            old = prefix
            prefix += max[0]

            for word in strs:
                if not word.startswith(prefix):
                    return old

            pos += 1
            frequency = {}
            

        return prefix
        
        