class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_ab = {}
        count = 0
        
        for a in nums1:
            for b in nums2:
                if a + b in sum_ab:
                    sum_ab[a + b] += 1
                else:
                    sum_ab[a + b] = 1
