class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> map = new HashMap<>();
    
        for(int i = 0; i < s.length(); i++) {
            char c1 = s.charAt(i); // character at i in string s
            char c2 = t.charAt(i); // character at i in string t
        
            if(map.containsKey(c1)) { // if the dictionary contains c1
                if(map.get(c1) != c2) { // if c1 does match c2 which means the key leads to a different value
                    return false;  
                }
            } else { // dictionary does not contain c1
                if(map.containsValue(c2)) { // if dictionary contains the value of c2 return false 
                    return false; // because c2 would map to a multiple c1 values
                }
                map.put(c1, c2); // add c1 as key and c2 as value
            }
        }
    
    return true;
    }
}
