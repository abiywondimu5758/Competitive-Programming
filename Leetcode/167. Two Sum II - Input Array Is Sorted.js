/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    pointer1 = 0
    pointer2 = numbers.length-1

    while(pointer1 < pointer2){
    if(numbers[pointer1] + numbers[pointer2] > target){
        pointer2--;
    }
    else if(numbers[pointer1] + numbers[pointer2] < target){
        pointer1++
    }
    else{
        return[pointer1+1,pointer2+1]
    }
    }
};
