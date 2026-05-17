class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""

        if len(word1) > len(word2):
            add_idx = len(word1) - len(word2)
            add = word1[-add_idx:]
        elif len(word1) < len(word2):
            add_idx = len(word2) - len(word1)
            add = word2[-add_idx:]
        else:
            add = ""

        for w1, w2 in zip(word1, word2):
            merged += w1 + w2
        
        merged += add

        return merged