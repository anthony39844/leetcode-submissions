class Solution {
    public void moveZeroes(int[] nums) {
        int zeroCount = nums.length;
        int[] copy = new int[nums.length];
        for (int i = 0; i < nums.length; i++){
            copy[i] = nums[i];
        }
        int index = 0;
        for (int i = 0; i < nums.length; i++){
            if (copy[i] != 0){
                nums[index] = copy[i];
                index++;
                zeroCount--;
            }
        }
        for (int i = nums.length - zeroCount; i < nums.length; i++){
            nums[i] = 0;
        }
    }
}
