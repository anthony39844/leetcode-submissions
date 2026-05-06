class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        if((r == mat.length && c == mat[0].length) || (mat.length * mat[0].length != r * c)) {
            return mat;
        }

        int newMat [][] = new int [r][c], rIndex = 0, cIndex = 0;

        for (int row = 0; row < mat.length; row++) {
            for (int col = 0; col < mat[0].length; col++) {
                if(cIndex == c) {
                    rIndex++;
                    cIndex = 0;
                }

                newMat[rIndex][cIndex++] = mat[row][col];
            }
        }

        return newMat;
    }
}
