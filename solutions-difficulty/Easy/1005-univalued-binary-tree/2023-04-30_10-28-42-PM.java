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
    public int count = 0;
    public boolean isUnivalTree(TreeNode root) {
        if (root == null){
            return true;
        }
        int val = root.val;
        int total = helper(root, val);
        if(total > 0){
            return false;
        }
        return true;
    }
    private int helper(TreeNode root, int val){
        if (root == null){
            return 0;
        }
        helper(root.left, val);
        helper(root.right, val);
        System.out.println(root.val);
        if (root.val != val){
            count++;
        }
        return count;
    }
}
