class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            b = float('-inf')
            temp = 0
            for k in range(1, 4):
                if i + k > n:
                    break
                temp += stoneValue[i + k - 1]
                b = max(b, temp - dp[i + k])
            dp[i] = b
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"