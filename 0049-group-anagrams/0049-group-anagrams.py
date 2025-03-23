class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_dict = {}

        for s in strs: #time complexity is O(n)

            sorted_s = ''.join(sorted(s)) #time complexity is O(n)* O(nlogn)

            if sorted_s not in strs_dict:
                strs_dict[sorted_s] = [s]
            else:
                strs_dict[sorted_s].append(s)
        
        return list(strs_dict.values()) #total time complexity is O(n)* O(n)* O(nlogn)