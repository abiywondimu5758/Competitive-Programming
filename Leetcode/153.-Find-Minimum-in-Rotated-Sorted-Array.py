class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)
        while low <= high and nums!=0:
            mid = (low + high) // 2
            if nums[mid] < nums[mid-1] or len(nums) == 1:
                return nums[mid]
            elif nums[mid] > nums[-1]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
