class Solution(object):
    def twoSum(self, nums, target):                    
        hashmap={}
        for i in range(len(nums)):
            find=target-nums[i]
            if find in hashmap:
                return [hashmap[find],i]
            hashmap[nums[i]]=i