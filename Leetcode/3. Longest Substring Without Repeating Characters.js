
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let counter = 0
    let map = new Map()
    let left = 0

    for(let right = 0; right < s.length; right++){
        let currentChar = s[right]
        if(map.has(currentChar) && map.get(currentChar) >= left){
            left = map.get(currentChar) + 1
        }
        map.set(currentChar,right)
        counter = Math.max(counter, right - left + 1)
    }
    return counter;
};
