class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        current = 0

        for n in nums:
            current += n
            ans.append(current)
            
        return ans