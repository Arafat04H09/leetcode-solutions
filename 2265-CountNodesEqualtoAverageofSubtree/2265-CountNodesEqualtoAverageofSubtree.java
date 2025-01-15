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
    private int count = 0;

    public int averageOfSubtree(TreeNode root) {
        averageHelper(root);
        return count;
    }

    public int[] averageHelper(TreeNode root) {
        if (root == null) {
            return new int[]{0, 0}; 
        }

        int[] left = averageHelper(root.left);
        int[] right = averageHelper(root.right);

        int sum = left[0] + right[0] + root.val;
        int nodes = left[1] + right[1] + 1;

        if (root.val == sum / nodes) {
            count++;
        }

        return new int[]{sum, nodes};
    }
}
