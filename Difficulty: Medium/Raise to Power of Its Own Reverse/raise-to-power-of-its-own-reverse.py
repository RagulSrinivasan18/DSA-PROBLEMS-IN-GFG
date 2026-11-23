class Solution:
    def reverseExponentiation(self, n):
        # code here
        s=str(n)
        p=s[::-1]
        r=int(p)
        return n**r
        