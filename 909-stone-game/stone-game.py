class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if len(piles) % 2 == 0:
            return True
        def get_max(i,j):
            if i == j:
                return piles[i]
            r = piles[j] - get_max(i,j - 1)
            l = piles[i] - get_max(i + 1,j)
            return max(r,l)
        return get_max(0,len(piles) - 1) >= 0