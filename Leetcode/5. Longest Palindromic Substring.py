class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        table = [[0 for _ in range(len(s))] for _ in range(len(s))]
        start,maxlen = 0,0
        for i in range(len(s)):
            table[i][i] = 1
            if i < len(s) - 1 and s[i] == s[i+1]:
                table[i][i+1] = 1 
                start = i
                maxlen = 2

