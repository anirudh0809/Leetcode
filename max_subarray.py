"""
Given an integer array nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


Input: nums = [1]
Output: 1


Input: nums = [-1]
Output: -1

Input: nums = [-100000]
Output: -100000
"""
# Brute force
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         subsum = float("-inf")
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                tmp = sum(nums[i:j])
                if subsum < tmp:
                    subsum = tmp
        return subsum

# Kadane's Algo
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0: return -1
        maxsub = [None]*length
        maxsub[0] = nums[0]
        for i in range(1,length):
            maxsub[i] = max(nums[i],maxsub[i-1]+nums[i])
        return max(maxsub)