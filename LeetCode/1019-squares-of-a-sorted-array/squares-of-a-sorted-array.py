class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_array = []
        for num in nums:
            new_array.append(num**2)
        
        ans = sorted(new_array)

        return ans