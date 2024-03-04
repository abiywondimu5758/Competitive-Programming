
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

O(n) time
var topKFrequent = function(nums, k) {
    let map = new Map()

    for(let num of nums){
        map.set(num, (map.get(num) || 0) +1)
    }

    let buckets = new Array(nums.length + 1).fill().map(()=>[])
    for(let [num,freq] of map){
        buckets[freq].push(num)
    }

    result = []
    for(let i = buckets.length-1; i>=0 && result.length<k;i--){
        result.push(...buckets[i]);
    }
    return result;
    // return Object.entries(map).sort((a,b)=> b[1]-a[1]).slice(0,k).map(([key,value])=>parseInt(key))

};
