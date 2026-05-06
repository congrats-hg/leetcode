class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # target에 빈 리스트 할당
        # index array의 인덱스 번호로 nums array의 요소를 target에 추가

        target = []

        for num, idx in zip(nums, index):
            target.insert(idx, num)
        
        return target