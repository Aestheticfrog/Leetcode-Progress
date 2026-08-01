class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        def get_max(i,j):
            if i == j:
                return nums[i]
            r = nums[j] - get_max(i,j - 1)
            l = nums[i] - get_max(i + 1,j)
            return max(r,l)
        return get_max(0,len(nums) - 1) >= 0