class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs,key=len)
        smallest = strs[0]
        res=''
        print('smallest',smallest)
        for x in range(0,len(smallest)):
            for i in range (1,len(strs)):
                if strs[0][x] != strs[i][x]:
                    return res
            res += strs[0][x]
        return res
        
        
        