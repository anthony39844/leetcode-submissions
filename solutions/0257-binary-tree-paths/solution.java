/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> paths = new ArrayList<>();
        dfs(root, new ArrayList<>(), paths);
        return paths;
    }
    
    private void dfs(TreeNode node, List<String> path, List<String> paths) {
        if (node == null) return;
        
        path.add(Integer.toString(node.val));
        
        if (node.left == null && node.right == null) {
            paths.add(String.join("->", path));
        } else {
            dfs(node.left, path, paths);
            dfs(node.right, path, paths);
        }
        
        path.remove(path.size() - 1);
    }
}
