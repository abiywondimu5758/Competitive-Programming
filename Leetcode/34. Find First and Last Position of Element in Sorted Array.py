class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLow(nums,target):
            low, high = 0, len(nums)-1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid]<target:
                    low = mid + 1
                else:
                    high = mid -1                
            return low
        def searchHigh(nums,target):
            low, high = 0, len(nums)-1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid]<=target:
                    low = mid + 1
                else:
                    high = mid -1                
            return high
        
        low = searchLow(nums,target)
        high = searchHigh(nums,target)
        if low <= high:
            return [low,high]
        else:
            return[-1,-1]
