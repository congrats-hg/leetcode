class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                ans = [left+1, right+1]
                return ans
            else:
                if two_sum < target:
                    left += 1
                else:
                    right -= 1