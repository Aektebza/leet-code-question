class Solution(object):
    def minOperations(self, nums, k):
        a=sum(nums)
        s=a//k
        i=a-s*k
        return i