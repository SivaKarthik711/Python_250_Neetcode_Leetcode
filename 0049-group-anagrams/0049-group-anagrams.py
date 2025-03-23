class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_dict = {}

        for s in strs:

            sorted_s = ''.join(sorted(s))

            if sorted_s not in strs_dict:
                strs_dict[sorted_s] = [s]
            else:
                strs_dict[sorted_s].append(s)
        
        result list(strs_dict.values())