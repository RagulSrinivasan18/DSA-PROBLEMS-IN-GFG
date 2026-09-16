class Solution:
    def rotate(self, arr):
        k=1
        arr[:]=arr[-k:] + arr[:-k]
        
        return arr
        