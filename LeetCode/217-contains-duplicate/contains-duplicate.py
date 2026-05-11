class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1. 한 번 봤던 정수를 s(t: set)에 저장
        # 2. 해당 정수가 s(t: set)에 있으면 True 반환, 끝까지 없으면 False 반환

        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False