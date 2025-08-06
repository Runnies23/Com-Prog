class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        ## Method 2
        total = sum(nums[:k])
        max_val = total

        for i in range(k, len(nums)):
            total = total + nums[i] - nums[i-k]
            max_val = max(max_val, total)

        return max_val / float(k)


runner = Solution()
print(runner.findMaxAverage([-1],1))