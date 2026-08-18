from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s) # look like: ['a','b','c',...]
        sorted_t = sorted(t) # ['','','',...]

        s_count = defaultdict() # it is a blank dictionary as {'letter'->str : count->int}
        t_count = defaultdict() # it is a balnk dictionary as {'letter' : count}
        

        for i in sorted_s:
            if i in s_count: # this line is possible , only because s_count is a dictionary, and i is considered as the key of that dictionary
                s_count[i]+= 1   # adding 1 to that value in s_count dictionary
            else: s_count[i]= 1

        
        for j in sorted_t:
            if j in t_count:
                t_count[j]+=1
            else: t_count[j]=1

        return s_count == t_count


        '''
        if len(s) != len(t):
            return false
        
        return sorted(s)==sorted(t) # sorted always returns a list of separate letters. Output: ['a', 'c', 't'] 
        '''
'''
My_Comments:
so, i have solved this problem using HASH MAPS concept, by creating two dictionaries which helped me to count letter by letter and finally checking if the 2 dicts are exactly equal. 
'''
        