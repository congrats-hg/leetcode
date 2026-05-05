class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = len(words)

        for w in words:
            w = "".join(set(w))
            for letter in w:
                if letter not in allowed:
                    ans -= 1
                    break

        return ans