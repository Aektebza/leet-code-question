#my solution
class Solution2(object):
    def findLucky(self, arr):
        b=-1
        for a in arr:
            c=0
            for i in arr:
                if a==i:
                    c+=1
            if c==a:
                if c==max(arr):
                    return(c)
                elif c>b:
                    b=c
        return (b)  
    
#best solution
# class Solution1(object):
#     def findLucky(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: int
#         """
#         freq=Counter(arr)
#         maxL=-1
#         for item,value in freq.items():
#             if(item==value and item>maxL):
#                 maxL=item
#         return maxL