class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pos = 0
        prefix = ""

        while True:

            temp = strs[0][:pos+1]
            for word in strs:
                if not word.startswith(temp) or len(word) == len(prefix):
                    return prefix

            prefix = strs[0][:pos+1]
            pos += 1
        
        