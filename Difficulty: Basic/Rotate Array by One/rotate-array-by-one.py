class Solution:
    def rotate(self, arr: list[int]) -> None:
        # code here
        arr[:]=arr[-1:]+arr[:-1]
        return arr
        