class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] + 1:
                max_sum += nums[i]
            else:
                break 
        while True:
            if max_sum in nums:
                max_sum += 1
            else:
                return max_sum
        
