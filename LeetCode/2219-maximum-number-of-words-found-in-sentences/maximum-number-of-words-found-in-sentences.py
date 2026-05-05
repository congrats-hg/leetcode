class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_num = 0

        for s in sentences:
            num = len(s.split())
            if num > max_num:
                max_num = num

        ans = max_num

        return ans