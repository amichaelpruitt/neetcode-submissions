class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        candidate = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
                if candidate < curr:
                    candidate = curr            
            else: curr = 0
        return candidate