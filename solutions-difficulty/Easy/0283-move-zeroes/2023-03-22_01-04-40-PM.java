class Solution {
    public void moveZeroes(int[] nums) {
        int zeroCount = 0;
        int[] copy = new int[nums.length];
        for (int i = 0; i < nums.length; i++){
            copy[i] = nums[i];
        }
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == 0){
                zeroCount++;
            } 
        }
        int index = 0;
        for (int i = 0; i < nums.length; i++){
            if (copy[i] != 0){
                nums[index] = copy[i];
                index++;
            }
        }
        for (int i = nums.length - zeroCount; i < nums.length; i++){
            nums[i] = 0;
        }
    }
}
