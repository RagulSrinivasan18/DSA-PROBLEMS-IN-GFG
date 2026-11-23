class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        
        a=[0,1]
        def fibo(i,j):
            nonlocal a
            i,j=j,i+j
            
            if len(a)<=n:
                a.append(j)
                fibo(i,j)
        
        fibo(0,1)
        return a[n]
            
            
            
            