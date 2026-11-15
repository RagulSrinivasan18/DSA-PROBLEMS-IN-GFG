class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        cursum=0
        maxi=arr[0]
        for i in range(len(arr)):
            cursum+=arr[i]
            
            maxi=max(cursum,maxi)
            
            if cursum<0:
                cursum=0
        return maxi
            
            
            