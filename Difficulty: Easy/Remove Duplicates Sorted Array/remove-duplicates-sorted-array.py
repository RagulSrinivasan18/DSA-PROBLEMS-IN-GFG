class Solution:
    def removeDuplicates(self, arr):
        # code here 
        c=[]
        for i in range(len(arr)):
            if i==0 or arr[i]!=arr[i-1]:
                c.append(arr[i])
        return c