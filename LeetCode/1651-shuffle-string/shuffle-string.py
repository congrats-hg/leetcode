class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic = {}

        for idx, i in enumerate(indices):
            dic[i] = s[idx]
        
        dic = dict(sorted(dic.items()))
        ans = ""
        for v in dic.values():
            ans += v
        
        return ans