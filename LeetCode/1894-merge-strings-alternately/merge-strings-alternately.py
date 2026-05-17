class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        word1_len = len(word1)
        word2_len = len(word2)

        if word1_len > word2_len:
            add_idx = word1_len - word2_len
            add = word1[-add_idx:]
        elif word1_len < word2_len:
            add_idx = word2_len - word1_len
            add = word2[-add_idx:]
        else:
            add = ""

        for w1, w2 in zip(word1, word2):
            merged.append(w1)
            merged.append(w2)
        
        merged.append(add)
        ans = "".join(merged)

        return ans