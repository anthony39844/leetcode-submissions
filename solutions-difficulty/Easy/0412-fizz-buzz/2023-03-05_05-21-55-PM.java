class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> list=new ArrayList<String>(); 
        for (int i = 1; i <= n; i++){
            String s = Integer.toString(i);
            if (i % 3 == 0 && i % 5 == 0){
                list.add(i - 1, "FizzBuzz");
            }else if (i % 3 == 0){
                list.add(i - 1, "Fizz");
            }else if (i % 5 == 0){
                list.add(i - 1, "Buzz");
            }else{ list.add(s);}
        } 
        return list;
    }
}
