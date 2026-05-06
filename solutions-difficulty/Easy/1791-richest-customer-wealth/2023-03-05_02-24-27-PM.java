class Solution {
    public int maximumWealth(int[][] accounts) {
        int prev = 0;
        int max = 0;
        for (int i = 0; i < accounts.length; i++){
            prev = 0;
            for (int j = 0; j < accounts[i].length; j++){
                prev += accounts[i][j];
            }
            if (prev > max){
                max = prev;
            }
        }
        return max;
    }
}
