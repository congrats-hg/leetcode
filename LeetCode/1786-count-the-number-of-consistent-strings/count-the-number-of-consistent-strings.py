class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowed_set = set(allowed)

        for w in words:
            if set(w) <= allowed_set:
                ans += 1

        return ans