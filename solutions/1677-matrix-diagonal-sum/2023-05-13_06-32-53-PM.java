class Solution {
    public int diagonalSum(int[][] mat) {
        int sum = 0,length = mat.length - 1;;
        if (mat.length % 2 == 0){
           for (int i = 0; i < mat.length; i++){
                sum += mat[i][i];
                sum += mat[i][length--];
            } 
        }else{
            int mid = mat.length / 2;
            for (int i = 0; i < mat.length; i++){
                sum += mat[i][i];
                sum += mat[i][length--];
            }
            sum -= mat[mid][mid];
        }
        return sum;
    }
}
