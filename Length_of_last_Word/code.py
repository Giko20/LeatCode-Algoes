# code
'''python'''

class Solution(object):
    def lengthOfLastWord(self, s):
        self.s=s
        string = self.s.strip().split(' ')[-1]
        return len(string)
