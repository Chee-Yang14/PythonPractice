class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hold = {}
        
        for i in strs:
            sortedstr = "".join(sorted(i))
            if(hold.__contains__(sortedstr)==False):
               hold[sortedstr] = []
            hold[sortedstr].append(i)

        return hold.values()