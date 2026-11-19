class Solution:
    def rotateMatrix(self, mat: list[list[int]]) -> None:
        # code here
        n=len(mat)
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
                
        for j in range(n):
            l=0
            r=n-1
            
            while l<r:
                mat[l][j],mat[r][j]=mat[r][j],mat[l][j]
                l+=1
                r-=1
                
        return mat