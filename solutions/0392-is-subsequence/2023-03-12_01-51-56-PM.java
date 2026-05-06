class Solution {
    public boolean isSubsequence(String s, String t) {
        int sIndex = 0, tIndex = 0; 
    
        while (sIndex < s.length() && tIndex < t.length()) { 
            if (s.charAt(sIndex) == t.charAt(tIndex)) { 
                //if character at sIndex is equal to character at tIndex then increase sIndex
                sIndex++;
                
            }
            tIndex++;
            // else increase tIndex to compare character at sIndex to the next letter in t
        } // 
        // the while loop will stop running when t or s is not less than the length of the string
        // and so if t reaches that first then s will not be == to s.length and will return false, which means
        // not all letters in s could be found in t
        // if sIndex == s.length that means all letter in s were found in t and they were in the same order
        // and it will also return true
        return sIndex == s.length();
    }
}
