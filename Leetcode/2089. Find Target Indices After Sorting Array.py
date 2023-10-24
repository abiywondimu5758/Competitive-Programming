class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i,j in enumerate(sorted(nums)) if j == target]
