class Solution {
    public int searchInsert(int[] nums, int target) {
        int high = nums.length;
        int low = 0;
        int index = 0;
        while (high - low > 0){
            int mid = low + (high - low) / 2; 
            if (target == nums[mid]){ 
                return mid;
            }else if (target > nums[mid]){
                low = mid + 1;
            }else{
                high = mid - 1; 
            }
        }
        int count = 0;
        if (target > nums[nums.length - 1]){
            return nums.length;
        }
        while (target > nums[count]){
            count++;
            index = count;
        }
        return index;
        
    }
}
