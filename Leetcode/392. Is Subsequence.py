class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i==len(s)
# JS
# /**
#  * @param {string} s
#  * @param {string} t
#  * @return {boolean}
#  */
# var isSubsequence = function(s, t) {
#     let pointer1 = 0
#     let pointer2 = 0

#     while(pointer2 < t.length){
#         if(s[pointer1] === t[pointer2]){
#             pointer1++;
#             pointer2++;
#         }
#         else {
#             pointer2++; 
#         }
#     }
#     return pointer1 === s.length
# };
