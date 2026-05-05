from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        counter_stones = Counter(stones)

        for letter in jewels:
            ans += counter_stones[letter]
        
        return ans