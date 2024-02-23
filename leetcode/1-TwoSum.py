class Solution(object):
    def twoSUm(self, nums, target):
        hashmap = {}
        for i in nums:
            if(target - nums[i] in hashmap):
                return {hashmap[target - nums[i]],i}
            hashmap[nums[i]] = i