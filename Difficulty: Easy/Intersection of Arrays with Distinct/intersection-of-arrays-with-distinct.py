class Solution:
    def findIntersection(self, a: list[int], b: list[int]) -> list[int]:
        # code here
        c=[]
        b=set(b)
        for i in range(len(a)):
            if a[i] in b:
                c.append(a[i])
                
        return c