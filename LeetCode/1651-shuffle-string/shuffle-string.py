class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lst = [""]*len(s)

        for s_idx, idx in enumerate(indices):
            lst[idx] = s[s_idx]
        
        ans = "".join(lst)

        return ans