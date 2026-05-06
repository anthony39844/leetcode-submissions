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
        // int diff = 0;
        // for (int i = 0; i < prices.length; i++){
        //      for (int j = i + 1; j < prices.length; j++){
        //          if ((prices[j] - prices[i]) > diff){
        //              diff = prices[j] - prices[i];
        //          }
        //      }
        // }
        return diff;
    }
}
