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
    private int sum = 0;
    public int sumRootToLeaf(TreeNode root) {
        sumHelper(root, 0);
        return sum;
    }

    public void sumHelper(TreeNode root, int curSum) {
        if (root == null) {
            return;
        }

        curSum = (curSum << 1) | root.val;
        if (root.left == null && root.right == null) {
            sum += curSum;
            return;
        }

        sumHelper(root.left, curSum);
        sumHelper(root.right, curSum);
    }
}