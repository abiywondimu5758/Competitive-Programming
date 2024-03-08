/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let str = s.replace(/[^a-zA-Z0-9]/g,'').toLowerCase();
    let pointer1=0
    let pointer2=str.length-1;
    while(pointer1<=pointer2){
        if(str[pointer1]==str[pointer2]){
            pointer1++;
            pointer2--;
        }
        else{
            return false
        }
    
    }
    return true
};
