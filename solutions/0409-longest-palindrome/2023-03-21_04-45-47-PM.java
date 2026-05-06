class Solution {
    public int longestPalindrome(String s) {
        int amount = 0;
        Map<Character, Integer> map = new HashMap<>();
        boolean odd = false;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        for (int num : map.values()){
            if (num % 2 == 0){
                amount += num;
            }else {
                amount += num - 1;
                odd = true;
            }
        }
        if (odd){
            amount++;
        }
        return amount;
    }
}
