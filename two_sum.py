"""This beat 99.32% of python submissions"""

class Solution(object):
    def twoSum(self, nums, target):
        nums_len=len(nums)
        map={}
        for i in range(nums_len):
            map[nums[i]]=i
        for i in range(nums_len):
            complement=target-nums[i]
            try:
                if map[complement]!=i:
                    return [i,map[complement]]
            except KeyError:
                continue