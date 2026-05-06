class Solution {
    public int arraySign(int[] nums) {
        int negCount = 0, zeroCount = 0;
        for (int i : nums){
            if (i < 0){
                negCount++;
            }
            if (i == 0){
                zeroCount++;
            }
        }
        if (zeroCount != 0){
            return 0;
        }
        if (negCount % 2 == 0){
            return 1;
        }
        return -1;
    }
}
