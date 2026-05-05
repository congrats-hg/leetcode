class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans_lst = []

        for s in sentences:
            count = len(s.split())
            ans_lst.append(count)
        
        ans = max(ans_lst)

        return ans