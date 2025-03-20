class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: # to check given list strs is empty or not.
            return "" # if the case return empty string
        
        temp = strs[0] #take first element of the list to check with string in the the list

        for i in range(1, len(strs)): # index starts with 1 to end of the given list strs
            while not strs[i].startswith(temp): # need to cut down the string whenever the "i" value in list strs is not same as temp
                temp = temp[:-1] 
            if not temp: #if temp is empty string
                return ""
        
        return temp