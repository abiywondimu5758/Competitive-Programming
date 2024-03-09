
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let buy = 0
    let sell = 1
    let maxProfit = 0

    while(sell<prices.length){
        if(prices[buy]>prices[sell]){
            buy = sell
        }
        else{
            let profit = prices[sell] - prices[buy]
            maxProfit = Math.max(maxProfit,profit)
        }
        sell++;
    }
    return maxProfit;
};
