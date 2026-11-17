class Solution:
    def findTriplets(self, arr):
        #code here
        arr.sort()
        for i in range(2,len(arr)):
            l=0
            r=i-1
            if len(arr)<3:
                continue
            
            while l<r:
                target=arr[l]+arr[r]+arr[i]
                
                if target==0:
                    return True
                elif target<0:
                    l+=1
                else:
                    r-=1
        return False
        