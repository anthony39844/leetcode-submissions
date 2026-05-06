class Solution {
    public void sortColors(int[] nums) {
        for (int i = 1; i < nums.length; i++){
            int temp;
            if (nums[i] < nums[i - 1]){
                for (int j = i; j > 0; j--){
                    if (nums[j] < nums[j - 1]){
                    temp = nums[j - 1];
                    nums[j - 1] = nums[j];
                    nums[j] = temp;
                    }     
                }
            }
            
        }
    }
}
