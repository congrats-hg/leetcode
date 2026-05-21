class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        is_consecutive = []

        for num in arr:
            if num % 2 == 1:
                is_consecutive.append(num)
            else:
                is_consecutive = []
            
            if len(is_consecutive) == 3:
                return True
        
        return False