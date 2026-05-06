class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        List<Integer> repeated = new ArrayList<Integer>();
        for (int num : nums1){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        for (int num : nums2){
            if (map.containsKey(num) && map.get(num) > 0){
                repeated.add(num);
                map.put(num, map.get(num) - 1);
            }
        }
        int[] intersect = new int[repeated.size()];
        for (int i = 0; i < repeated.size(); i++){
            intersect[i] = repeated.get(i);
        }
    
        return intersect;
    }
}
