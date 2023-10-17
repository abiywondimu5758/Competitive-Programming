#1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high and len(nums) !=0:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1
        return -1
#2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def count_rotations_binary(nums):
            lo = 0
            hi = len(nums)-1
            
            while lo<=hi and len(nums)!=0:
                mid = (lo+hi)//2
                mid_number = nums[mid]
                
                # Uncomment the next line for logging the values and fixing errors.
        #         print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
                
                if mid > 0 and mid_number < nums[mid-1]:
                    # The middle position is the answer
                    return mid
                
            
                
                elif mid_number < nums[-1]:
                    # Answer lies in the left half
                    hi = mid - 1  
        
                else:
                    # Answer lies in the right half
                    lo = mid + 1
    
            return 0
        def binary_search(lo, hi, condition):
            while lo <= hi:
                mid = (lo + hi) // 2
                result = condition(mid)
                if result == 'found':
                    return mid
                elif result == 'left':
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1
        result = count_rotations_binary(nums)
        list1 = nums[:result]
        list2 = nums[result:]
        def condition(mid):
            if list1[mid] == target:
                if mid > 0 and list1[mid-1] == target:
                    return 'left'
                else:
                    return 'found'
            elif list1[mid] > target:
                return 'left'
            else:
                return 'right'
        def condition1(mid):
            if list2[mid] == target:
    #             print(list2[mid])
                if mid > 0 and list2[mid-1] == target:
                    return 'left'
                else:
                    return 'found'
            elif list2[mid] > target:
                return 'left'
            else:
                return 'right'
        if binary_search(0, len(list1)-1, condition)!=-1:
            return binary_search(0, len(list1)-1, condition)
        elif binary_search(0, len(list2)-1, condition1)==-1:
            return -1
        else:
            return result + binary_search(0, len(list2)-1, condition1)
