/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let t = s.trim()
    let words = t.split(' ')
    return words[words.length-1].length
};
