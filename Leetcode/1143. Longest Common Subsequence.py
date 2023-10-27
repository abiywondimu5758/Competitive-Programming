#Solution using dictionary
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def recursion(t1:int,t2:int):
            key = t1,t2
            if key in memo:
                return memo[key]
            elif t1 == len(text1) or t2 == len(text2):
                memo[key] = 0
            elif text1[t1] == text2[t2]:
                memo[key] = 1 + recursion(t1 + 1, t2 + 1)
            else:
                memo[key] = max(recursion(t1 + 1, t2), recursion(t1, t2 + 1))
            return memo[key]
        return recursion(0,0)
