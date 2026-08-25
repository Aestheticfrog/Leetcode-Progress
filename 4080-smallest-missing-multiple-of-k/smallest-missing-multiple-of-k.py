class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        i = 1
        while True:
            t = i * k
            if t not in nums:
                return t
            i += 1
