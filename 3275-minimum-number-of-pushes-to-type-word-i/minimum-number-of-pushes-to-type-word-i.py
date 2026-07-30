class Solution:
    def minimumPushes(self, word: str) -> int:
        l = len(word)
        if l == 8:
            return 8
        elif l < 8:
            return l
        else:
            res = 0
            i = 0
            while l > 8:
                l -= 8
                i += 1
                res += i * 8
            res += l * (i + 1)
            return res