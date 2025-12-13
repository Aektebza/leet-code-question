class Solution(object):
    def longestCommonPrefix(self, strs):
        num=0
        ans=9999999999999
        if len(strs)==1:
            return strs[0]
        for i in range(0,len(strs)-1):
            num=0
            for a in range(0,len(strs[i])):
                print(i,a,strs[i][a])
                if a<len(strs[i+1]):
                    if strs[i][a] == strs[i+1][a]:
                        num+=1
                    else:
                        break
            if num<ans:
                ans=num
        return(strs[0][0:ans])