

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequent = {}
        for number in nums:
            if number not in frequent:
                frequent[number] = 1; 
            else:
                frequent[number] = frequent[number]+1
        
        sorted_items = sorted(frequent.items(), key=lambda x: (-x[1], nums.index(x[0])))
        return [item[0] for item in sorted_items[:k]]