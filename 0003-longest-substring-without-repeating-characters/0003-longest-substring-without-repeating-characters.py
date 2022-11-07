class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            max = 0
            length = len(s)

            for i in range(0, length):

                count = 0
                dic = {}
                for j in range(i, length):

                    if s[j] in dic:
                        break
                    else:
                        dic[s[j]] = j
                        count +=1

                if count > max:
                    max = count

            return max