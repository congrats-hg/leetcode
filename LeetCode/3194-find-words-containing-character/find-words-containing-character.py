class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []

        for idx, s in enumerate(words):
            if x in s:
                ans.append(idx)
        
        return ans