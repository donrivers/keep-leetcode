class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        f = 0
        for n in nums:
            if nums[f] != n:
                f += 1
                nums[f] = n
        return len(nums) and f+1
        
