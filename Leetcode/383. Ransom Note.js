/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    let ransomNoteMap = new Map();
    let magazineMap = new Map();

    for(let char of ransomNote){
        ransomNoteMap.set(char, (ransomNoteMap.get(char) || 0) +1);
    }
    for(let char of magazine){
        magazineMap.set(char, (magazineMap.get(char) || 0) +1);
    }

    for( let [char, count] of ransomNoteMap){
        if(!magazineMap.has(char) || magazineMap.get(char) < count){
            return false;
        }
    }

    return true

};
