/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    let map = new Map()
    for(let num in nums){
        if(map.has(nums[num]) && num-map.get(nums[num])<=k){
            return true
        }
        map.set(nums[num], num)
    }
    return false;
};
