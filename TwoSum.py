#One pass solution. Accepted on Leetcode
#Time complexity - O(n)
#space complexity - O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(0,len(nums)):
            if (target - nums[i]) in dict1:
                return [i,dict1[target-nums[i]]]
            else:
                dict1[nums[i]] = i
        return []