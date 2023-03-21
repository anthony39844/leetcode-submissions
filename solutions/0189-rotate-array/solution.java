class Solution {
    public void rotate(int[] nums, int k) {
        if (nums.length == 0 || k == 0) {
            return;
        }
        // If k is greater than the length of the array,
        // take the modulo to get the effective number of steps
        k = k % nums.length;

        // Reverse the entire array
        for (int i = 0, j = nums.length - 1; i < j; i++, j--) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
        
        // Reverse the first k elements
        for (int i = 0, j = k - 1; i < j; i++, j--) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }

        // Reverse the remaining elements
        for (int i = k, j = nums.length - 1; i < j; i++, j--) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
}
