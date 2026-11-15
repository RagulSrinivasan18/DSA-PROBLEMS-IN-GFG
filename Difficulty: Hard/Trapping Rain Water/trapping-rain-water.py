class Solution:
    def maxWater(self, arr):
        # code here
        l=0
        r=len(arr)-1
        lm=0
        rm=0
        water=0
        
        while l<r:
            if arr[l]<arr[r]:
                if arr[l]>=lm:
                    lm=arr[l]
                else:
                    water+=lm-arr[l]
                
                l+=1
            else:
                if arr[r]>=rm:
                    rm=arr[r]
                else:
                    water+=rm-arr[r]
                r-=1
        return water