class Solution {
    public void reverseString(char[] s) {
        int length = s.length;
        for (int i = 0; i < length; i++){
            char a = s[length - 1];
            s[length - 1] = s[i];
            s[i] = a;
            length--;
        }
    }
}
