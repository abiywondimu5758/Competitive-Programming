class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        
        def search(low,high,nums):
            while low <= high:
                mid = (low + high)//2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    return search(low,mid - 1,nums)
                else:
                    return search(mid + 1,high,nums)
            return low
        return search(lo,hi,nums)
        
