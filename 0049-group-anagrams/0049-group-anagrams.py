class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)

        for s in strs:
            
            count = [0]*26 # [0,0,0,,0,0,0,0,0,0,0,0,0,0..0]
            for char in s:
                count[ord(char)- ord("a")] += 1

            result[tuple(count)].append(s)
        return list(result.values())
        