class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        #count = 1
        for i in s:
            #if i in dict_s:
            #     dict_s[i] += 1
            # else:
            #     dict_s[i] = count
            dict_s[i] = dict_s.get(i,0) + 1
        
        dict_t = {}
        for i in t:
            # if i in dict_t:
            #     dict_t[i] += 1
            # else:
            #     dict_t[i] = count
                dict_t[i] = dict_t.get(i,0) + 1

        if dict_s == dict_t:
            return True
        else:
            return False