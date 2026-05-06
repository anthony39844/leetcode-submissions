class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{sr, sc});
        int rowLength = image.length;
        int colLength = image[0].length;
        boolean visited[][] = new boolean[rowLength][colLength];
        while (!queue.isEmpty()) {
            int[] current = queue.remove();
            int curRow = current[0];
            int curCol = current[1];
            if ((curCol - 1 >= 0) && image[curRow][curCol - 1] == image[curRow][curCol] && image[curRow][curCol] != color){ 
                queue.add(new int[]{curRow, curCol - 1});
            }
            if ((curCol + 1 < colLength) && image[curRow][curCol + 1] == image[curRow][curCol] && image[curRow][curCol] != color) {
                queue.add(new int[]{curRow, curCol + 1});
            }
            if ((curRow - 1 >= 0) && image[curRow - 1][curCol] == image[curRow][curCol] && (image[curRow][curCol] != color)){
                queue.add(new int[]{curRow - 1, curCol});
            }
            if ((curRow + 1 < rowLength) && image[curRow + 1][curCol] == image[curRow][curCol] && image[curRow][curCol] != color){
                queue.add(new int[]{curRow + 1, curCol});
            }
            image[curRow][curCol] = color;
        }
        return image;
    }
}
