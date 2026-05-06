class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int i = 0; i < n; i++){
            nums1[m] = nums2[i];
            m++;
        }
        Arrays.sort(nums1);
        // int temp = 0;
        // for (int i = 0; i < nums1.length; i++){
        //     for (int j = i + 1; j < nums1.length; j++){
        //         if (nums1[i] > nums1[j]){
        //             temp = nums1[i];
        //             nums1[i] = nums1[j];
        //             nums1[j] = temp;
        //         }
        //     }
        // }
    }
}
