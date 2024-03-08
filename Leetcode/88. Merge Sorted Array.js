/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let pointer1 = 0, pointer2 = 0 
    let merged = []

    while(pointer1<m && pointer2 <n){
        if(nums1[pointer1]<=nums2[pointer2]){
            merged.push(nums1[pointer1])
            pointer1++;
        }
        else {
            merged.push(nums2[pointer2])
            pointer2++;
        }
    } 

    while(pointer1 < m){
        merged.push(nums1[pointer1]);
        pointer1++
    }

    while(pointer2 < n){
        merged.push(nums2[pointer2]);
        pointer2++
    }
   for(let i = 0; i<merged.length;i++){
       nums1[i]=merged[i]
   }
    return nums1
};
