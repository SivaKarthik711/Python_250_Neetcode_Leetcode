class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list) # we use this because when there an empty list, it has no key, so by using the defauldict key default value is given

        for s in strs: # to loop though out the strs
            
            count = [0]*26 # [0,0,0,,0,0,0,0,0,0,0,0,0,0..0] # we are created index value for each element as per alphabets 0-25
            for char in s: # looping through the each character of the string
                count[ord(char)- ord("a")] += 1 # so suppose s ="eat", char = 'e', count[101-97] += 1, after loop = [1,0,0,0,1,...1,0,0,0,0,0]
 
            result[tuple(count)].append(s) #converting into tuple as immutable and unique key exits in dict
        return list(result.values())
        