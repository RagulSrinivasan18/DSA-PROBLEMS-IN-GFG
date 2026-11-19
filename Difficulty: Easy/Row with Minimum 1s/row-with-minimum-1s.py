class Solution:
    def minRow(self, mat: list[list[int]]) -> int:
        # code here
        b=[]
        for i in range(len(mat)):
            a=mat[i].count(1)
            b.append(a)
            
        mini=min(b)
        return b.index(mini)+1
        
            
            
                