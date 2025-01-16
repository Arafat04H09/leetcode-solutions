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
    private int maxDiameter = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        binaryHelper(root);
        return maxDiameter;
    }

    public int binaryHelper(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int depthLeft = 0;
        int depthRight = 0;

        if (root.left != null) {
            depthLeft += 1 + binaryHelper(root.left);
        }
        if (root.right != null) {
            depthRight += 1 + binaryHelper(root.right);
        }
        
        maxDiameter = Math.max(maxDiameter, depthLeft + depthRight);
        return Math.max(depthLeft, depthRight);
    }
}