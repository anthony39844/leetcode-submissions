class Solution {
    private static void reverse(char[] a){
        int length = a.length;
        for (int k = 0; k < length; k++){ // reverses the array
            char temp = a[length - 1];
            a[length - 1] = a[k];
            a[k] = temp;
            length--;
        }
    }
    public String reverseWords(String s) {
        String reversed = "";
        String[] words = s.split(" ");
        for (int i = 0; i < words.length; i++){ 
            char[] reverseChars = new char[words[i].length()]; // array of the letters in each word
            for (int j = 0; j < words[i].length(); j++){ // puts all letters in the array
                reverseChars[j] = words[i].charAt(j);
            }
            reverse(reverseChars);
            for (int l = 0; l < reverseChars.length; l++){
                reversed += reverseChars[l];
            }
            if (i + 1 < words.length){
                reversed += " ";
            }
        // String[] words = s.split(" "); // array of words in string
        // String reversed = "";
        // for (int i = 0; i < words.length; i++){ 
        //     char[] reverseChars = new char[words[i].length()]; // array of the letters in each word
        //     for (int j = 0; j < words[i].length(); j++){ // puts all letters in the array
        //         reverseChars[j] = words[i].charAt(j);
        //     }
        //     int length = reverseChars.length;
        //     for (int k = 0; k < length; k++){ // reverses the array
        //         char temp = reverseChars[length - 1];
        //         reverseChars[length - 1] = reverseChars[k];
        //         reverseChars[k] = temp;
        //         length--;
        //     }
        //     for (int l = 0; l < reverseChars.length; l++){
        //         reversed += reverseChars[l];
        //     }
        //     if (i + 1 < words.length){
        //         reversed += " ";
        //     }
        // }
        }
        return reversed;
    }
}
