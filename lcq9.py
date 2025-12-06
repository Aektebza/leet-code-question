class Solution(object):
    def isPalindrome(self, x):
        s=str(x) #change num to string
        c=0
        r=1
        for i in s:                    #check head an tail with a loop
            if i==s[-r]:
                c+=0
            else:
                c+=1
            r+=1
        if c==0:                        #c=check
            return(True)
        else:
            return(False)
        
        
#best solution
#x1=121
#x1_str=str(x1)
#rint( x1_str==x1_str(::-1) )