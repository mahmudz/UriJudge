class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		m = 0
		tmp=0
		for x,i in enumerate(nums):
			if(i==1):
				tmp+=1
			else:
				if(tmp>m):
					m = tmp
					tmp = 0
		if(tmp>m):
			m=tmp
		return m
s = Solution()

print(s.findMaxConsecutiveOnes(zzz))
