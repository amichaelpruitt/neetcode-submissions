class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        candidate = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
                if curr > candidate:
                    candidate = curr
            else: curr = 0
        return candidate

