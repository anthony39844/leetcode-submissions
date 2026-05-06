class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        int n = x;
        int count = 0;
        while (n != 0){
            n = n / 10;
            count++;
        }
        int l = count;
        int[] arr = new int[count];
        for (int i = 0; i < count; i++){
            int digit = x % 10;
            arr[i] = digit;
            x /= 10;
        }
        int[] arr2 = new int[count];
        int j = 0;
        for (l = count - 1; l >= 0; l--){
            arr2[j] = arr[l];
            j++;
        }
        int equal = 0;
        for (int k = 0; k < arr.length; k++){
            if (arr[k] == arr2[k]){
                equal++;
            }
        }
        if(equal == count){
            return true;
        }
        return false;
    }
}
