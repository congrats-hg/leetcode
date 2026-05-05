class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lst = s.split()
        ans_lst = lst[:k]
        ans = " ".join(ans_lst)

        return ans