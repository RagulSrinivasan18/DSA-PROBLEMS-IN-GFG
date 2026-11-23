class Solution:
    def printTillN(self, n):
    	#code here 
    	a=[]
    	def solve(i):
    	    
    	    if i<=n:
    	        print(i,end=' ')
    	        
    	        solve(i+1)
    	solve(1)
    	return a
    	    