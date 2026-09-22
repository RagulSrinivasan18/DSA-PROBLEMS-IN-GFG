class Solution:
    def isSubset(self, a, b):
        # code here
        c=dict()
        
        for i in a:
            c[i] = c.get(i,0) +1
            
        for i in b:
            if i in c and c[i]>0:
                c[i]=c[i]-1
            else:
                return False
        
        return True
        
                