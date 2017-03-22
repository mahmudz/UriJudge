class Solution(object):
	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if(len(nums)):
			return []
		m = max(nums)
		nums = set(nums)
		s = set(i for i in range(1,m+1))
		resp = list(s- nums)
		return resp
s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

