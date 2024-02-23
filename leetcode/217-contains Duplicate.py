def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = set()
        for i in nums:
           if i in hashmap:
               return True
           hashmap.add(i)
        return False
    
