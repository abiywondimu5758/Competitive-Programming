class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ls = []
        n = len(nums) -1
        for i in range(n-1):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    ls.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                        continue
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return ls
