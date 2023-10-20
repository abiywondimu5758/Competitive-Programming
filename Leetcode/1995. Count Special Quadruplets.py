class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        i=0
        for a, b, c, d in combinations(nums, 4):
            if a + b + c == d:
                i += 1
        return i
