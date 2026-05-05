class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_dic = {}
        for i, n in enumerate(nums):
            nums_dic[i] = n
        
        ans = 0
        for i, i_value in nums_dic.items():
            for j, j_value in nums_dic.items():
                if i >= j:
                    pass
                else:
                    if i_value == j_value:
                        ans += 1
                    else:
                        pass
        
        return ans