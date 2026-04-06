class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        #print(hashset)
        longest = 0
        for num in nums:
            if num-1 not in hashset:
                current = 1
                i = 1
                #print("pas dans le hashset",num-1)
                while num+i in hashset:
                    #print('while')
                    current += 1
                    i += 1
                longest = max(current,longest)
                #print(longest)

        #print(longest)

        return longest
      