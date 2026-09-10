class Solution:
    def thirdLargest(self,arr):
        # code here
        
        arr.sort()
        if len(arr)<3:
            return -1
        
        a=arr[-3]
        
        return a
        