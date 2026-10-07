class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        
        arr.sort()
        
        for i in range(len(arr)-2):
            l=i+1
            r=len(arr)-1
            
            while l<r:
                if arr[i]+arr[l]+arr[r]==target:
                   return True
                elif arr[i]+arr[l]+arr[r]>target:
                    r-=1
                elif arr[i]+arr[l]+arr[r]<target:
                    l+=1
                else:
                    return False