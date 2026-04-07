class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1) -1
        m = len(word2) - 1
        res=''
        i = 0
        j = 0

        while i<=n or j<=m:
            if j>m:
                res += word1[i]
            elif i>n:
                res += word2[j]
            else:
                res += word1[i]+word2[j]
            i += 1
            j += 1
    
        return res

