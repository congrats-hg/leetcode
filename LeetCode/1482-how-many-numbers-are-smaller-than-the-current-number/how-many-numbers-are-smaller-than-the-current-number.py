class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        ans = []

        for i, n in enumerate(nums):
            if n not in dic.keys():
                dic[n] = 0
            else:
                continue
            
            for m in nums:
                if m < n:
                    dic[n] += 1
        
        for n in nums:
            ans.append(dic[n])
        
        return ans