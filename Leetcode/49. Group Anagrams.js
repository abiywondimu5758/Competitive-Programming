/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let anagrams = new Map()

    for(let str of strs){
        let counter = {}
        for(let char of str){
            counter[char] = (counter[char] || 0) +1
        }
        const key = Object.entries(counter).sort().join('')

        if(!anagrams.has(key)){
            anagrams.set(key, [])
        }
        anagrams.get(key).push(str)
    }
    return [...anagrams.values()]
};
