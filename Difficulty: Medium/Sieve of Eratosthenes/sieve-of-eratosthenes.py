class Solution:
    def sieve(self, n):
        # code here 
        prime=[True]*(n+1)
        prime[0]=False
        prime[1]=False
        
        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i,n+1,i):
                    prime[j]=False
        
        a=[]
        for i in range(n+1):
            if prime[i]:
                a.append(i)
        return a