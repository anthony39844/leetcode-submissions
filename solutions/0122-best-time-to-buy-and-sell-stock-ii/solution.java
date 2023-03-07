class Solution {
    public int maxProfit(int[] prices) {
        int count = 0;
        int i = 0;
        while (i < prices.length){
            for (int j = i+1; j < prices.length; j++){
                if ((prices[j] - prices[i]) > 0){
                    count += prices[j] - prices[i];
                    break;
                }else{break;}
            }
            i++;
        }
        return count;
    }
}
