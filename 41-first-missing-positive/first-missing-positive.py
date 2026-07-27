class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        target=1
        for i in nums:
            if i == target:
                target += 1
            elif i > target:
                return target
        return target

