class Solution:
    def rotateMatrix(self, k: int, mat: list[list[int]]) -> list[list[int]]:
        # code here 
        k=k%len(mat[0])
        for i in range(len(mat)):
            mat[i]=mat[i][k:]+mat[i][:k]
            
        return mat