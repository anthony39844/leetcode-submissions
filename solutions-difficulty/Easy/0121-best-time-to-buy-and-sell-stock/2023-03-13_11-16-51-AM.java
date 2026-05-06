class Solution {
    public int maxProfit(int[] prices) {
        int diff = 0;
        int min = 1000000;
        for (int i = 0; i < prices.length; i++){
             if (prices[i] < min){
                 min = prices[i];
             }else if (prices[i] - min > diff){
                diff = prices[i] - min;
             }
        }
        return diff;
    }
}
