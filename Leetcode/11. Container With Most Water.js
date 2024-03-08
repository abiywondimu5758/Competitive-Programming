
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let pointer1 = 0
    let pointer2 = height.length - 1
    let maxArea = 0
    while(pointer1 < pointer2){
        area = (pointer2 - pointer1) * Math.min(height[pointer1], height[pointer2])
        maxArea = Math.max(area,maxArea)
        if(height[pointer1]<height[pointer2]){
            pointer1++;
        }
        else if(height[pointer1]>height[pointer2]){
            pointer2--;
        }
        else{
            pointer1++;
            pointer2--;
        }

    }
    return maxArea;
};
