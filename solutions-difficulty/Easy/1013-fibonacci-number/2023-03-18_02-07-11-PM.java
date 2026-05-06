class Solution {
    public int fib(int n) {
        int prev = 0;
        int curr = 1;
        int total = 0;
        if (n == 1){
            return 1;
        }
        for (int i = 1; i < n; i++){
            total = prev + curr;
            prev = curr;
            curr = total;
        }
        return total;
    }
}
