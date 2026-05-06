class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<List<Integer>>();
    
        // If numRows is 0, return an empty list
        if (numRows == 0) {
            return triangle;
        }
        
        // Add the first row, which is always [1]
        triangle.add(new ArrayList<Integer>());
        triangle.get(0).add(1);
        
        // Generate the rest of the rows
        for (int rowNum = 1; rowNum < numRows; rowNum++) {
            List<Integer> row = new ArrayList<Integer>();
            List<Integer> prevRow = triangle.get(rowNum - 1);
            
            // Add the first element, which is always 1
            row.add(1);
            
            // Calculate the values in the current row
            for (int j = 1; j < rowNum; j++) {
                row.add(prevRow.get(j - 1) + prevRow.get(j));
            }
            
            // Add the last element, which is always 1
            row.add(1);
            
            // Add the current row to the triangle
            triangle.add(row);
        }
        
        return triangle;
    }
}
