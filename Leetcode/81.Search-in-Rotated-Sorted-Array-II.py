class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums)-1
        while low <= high and len(nums)!=0:
            mid = (low+high)//2
            if nums[mid] == target:
                return True
            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                elif nums[low] > target or nums[mid] < target:
                    low = low + 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                elif target > nums[high]  or nums[mid] > target:
                    high = high - 1
                else:
                    high = mid - 1
        return False
