class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        r = max(nums)
        l = min(nums)
        if len(nums) == (r - l + 1):
            return []
        res = []
        for i in range(l,r):
            if i not in nums:
                res.append(i)
        return res
