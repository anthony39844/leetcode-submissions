class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<List<Integer>> list = new ArrayList<>();
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        for (int i : nums1){
            int count = 0;
            for (int j = 0; j < nums2.length; j++){
                if (i == nums2[j]){
                    count++;
                }
            }
            if (count == 0){
                if (list1.contains(i)){
                    continue;
                }else{
                    list1.add(i);
                }
            }
        }
        for (int i : nums2){
            int count = 0;
            for (int j = 0; j < nums1.length; j++){
                if (i == nums1[j]){
                    count++;
                }
            }
            if (count == 0){
                if (list2.contains(i)){
                    continue;
                }else{
                    list2.add(i);
                }
            }
        }
        list.add(list1);
        list.add(list2);
        return list;
    }
}
