class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=[]
        c=nums.copy()
        for i in range(len(c)):
            if c[i] not in n:
                n.append(c[i])
            else:
                nums.remove(c[i])
        return len(nums)