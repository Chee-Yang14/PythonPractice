class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for index, i in enumerate(nums):
            for jindex, j in enumerate(nums):
                if(nums[index]==nums[jindex]):
                    continue
                elif len(ans)==0:
                    ans[index].append(j)
                else:
                    ans[index] = ans[index] * j
        return ans