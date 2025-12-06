class Solution(object):
    def romanToInt(self, s):
        n={
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        ans=0
        list_s=list(s)
        for i in range(len(list_s)):
            if i == len(list_s)-1:
                ans+=n[list_s[i]]
                break
            if n[list_s[i]]<n[list_s[i+1]]:
                ans-=n[list_s[i]]
            else:
                ans+=n[list_s[i]]
        return(ans)
