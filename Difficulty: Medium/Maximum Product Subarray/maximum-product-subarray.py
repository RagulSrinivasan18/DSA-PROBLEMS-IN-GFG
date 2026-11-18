class Solution:
	def maxProduct(self, arr):
		# code here
		minpro=arr[0]
		maxpro=arr[0]
		result=arr[0]
		
		for i in range(1,len(arr)):
		    
		    a=arr[i]
		    
		    maxi=max(a,a*maxpro,a*minpro)
		    mini=min(a,a*maxpro,a*minpro)
		    
		    minpro=mini
		    maxpro=maxi
		    
		    result=max(result,maxpro)
		return result
		    
		    