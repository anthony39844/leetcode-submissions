class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            int number = nums[i];
            if (map.containsKey(number)){
                return true;
            
            }else{
                map.put(number, number);
            }
        }
        return false;
    }
}
