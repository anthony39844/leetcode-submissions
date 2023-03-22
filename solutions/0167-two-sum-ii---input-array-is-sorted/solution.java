class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] indexArr = new int[2];
        int L = 0;
        int R = numbers.length - 1;
        while (L < R){
            if (numbers[L] + numbers[R] < target){
                L++;
            }else if (numbers[L] + numbers[R] > target){
                R--;
            }else{
                indexArr[0] = L + 1;
                indexArr[1] = R + 1;
                break;
            }
        }
        return indexArr;
    }
}
