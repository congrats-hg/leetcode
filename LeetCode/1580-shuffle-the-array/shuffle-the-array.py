class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_lst = nums[:n]
        y_lst = nums[n:]

        ans = []

        for x, y in zip(x_lst, y_lst):
            ans.append(x)
            ans.append(y)
        
        return ans