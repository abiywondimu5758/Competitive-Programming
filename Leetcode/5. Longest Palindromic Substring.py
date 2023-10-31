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
        for k in range(3,len(s) + 1):
            for i in range(len(s) - k + 1):
                j = i + k - 1
                if s[i] == s[j] and table[i+1][j-1] == 1:
                    table[i][j] = 1
                    if k > maxlen:
                        start = i
                        maxlen = k
        if start == 0 and maxlen == 0:
            maxlen += 1
        return s[start:start + maxlen]
