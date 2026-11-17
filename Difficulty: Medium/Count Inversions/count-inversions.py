class Solution:
    def inversionCount(self, arr):
        # code here
        def mergesort(arr,low,mid,high):
            left=low
            right=mid+1
            temp=[]
            count=0
            
            while(left<=mid and right<=high):
                if arr[left]<=arr[right]:
                    temp.append(arr[left])
                    left+=1
                else:
                    temp.append(arr[right])
                    count+=mid-left+1
                    right+=1
                
            while(left<=mid):
                temp.append(arr[left])
                left+=1
            while(right<=high):
                temp.append(arr[right])
                right+=1
                
            for i in range(low,high+1):
                arr[i]=temp[i-low]
                
            return count
                
        def merge(arr,low,high):
            count=0
            if low>=high:
                return count
            mid=(low+high)//2
            
            count+=merge(arr,low,mid)
            count+=merge(arr,mid+1,high)
            count+=mergesort(arr,low,mid,high)
            
            return count
        
        return merge(arr,0,len(arr)-1)
            
                