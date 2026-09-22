class Solution:
    def frequencyCount(self, arr):
        #  code here
        a=dict()
        b=[]
        for i in arr:
            a[i]=a.get(i,0) +1
        
        for i in range(1,len(arr)+1):
            
           c=a.get(i,0)
           b.append(c)
           
        return b
            
