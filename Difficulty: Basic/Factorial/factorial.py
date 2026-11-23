class Solution:
    def factorial(self, n: int) -> int:
        # code here
        a=1
        def solve(i):
            nonlocal a
            if i<=n:
                a*=i
                
                solve(i+1)
        solve(2)
        return a