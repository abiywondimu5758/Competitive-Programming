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



# JS
# var threeSum = function(nums) {
#     let arr = [];
#     nums.sort((a,b)=>a-b);

#     for (let i = 0; i < nums.length - 2; i++) {
#         if (i === 0 || nums[i] !== nums[i - 1]) {
#             let pointer1 = i + 1;
#             let pointer2 = nums.length - 1;
#             while (pointer1 < pointer2) {
#                 let sum = nums[i] + nums[pointer1] + nums[pointer2];
#                 if (sum === 0) {
#                     arr.push([nums[i], nums[pointer1], nums[pointer2]]);
#                     while (pointer1 < pointer2 && nums[pointer1] === nums[pointer1 + 1]) pointer1++;
#                     while (pointer1 < pointer2 && nums[pointer2] === nums[pointer2 - 1]) pointer2--;
#                     pointer1++;
#                     pointer2--;
#                 } else if (sum < 0) {
#                     pointer1++;
#                 } else {
#                     pointer2--;
#                 }
#             }
#         }
#     }
#     return arr;
# };
