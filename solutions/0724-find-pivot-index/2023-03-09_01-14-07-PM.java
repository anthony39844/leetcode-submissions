class Solution {
    public int pivotIndex(int[] nums) {
        int index = 0;
        int count = 0;
        for (int i = 0; i < nums.length; i++){
            int upperHalf = 0;
            int lowerHalf = 0;
            for (int j = i + 1; j < nums.length; j++){
                upperHalf += nums[j];
            }
            for (int k = i - 1; k >= 0; k--){
                lowerHalf += nums[k];
            }
            if (lowerHalf == upperHalf){
                index = i;
                count++;
                break;
            }
        }
        if (count == 0){
            return -1;
        }
        return index;
    }
}
