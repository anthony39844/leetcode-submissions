class Solution {
    public double average(int[] salary) {
        int max = 0, min = Integer.MAX_VALUE;
        double total = 0.0;
        for (int i = 0; i < salary.length; i++){
            if (salary[i] > max){
                max = salary[i];
            }
            if (salary[i] < min){
                min = salary[i];
            }
        }
        for (int i : salary){
            if (i != min && i != max){
                total += i;
            }
        }
        total = total / (salary.length - 2);
        return total;
    }
}
