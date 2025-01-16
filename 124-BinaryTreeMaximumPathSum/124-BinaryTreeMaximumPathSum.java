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
    private int maxPath = -1001;
    public int maxPathSum(TreeNode root) {
        dfs(root);
        return maxPath;
    }

    public int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftPathSum = root.val + dfs(root.left);
        int rightPathSum = root.val + dfs(root.right);
        int pathWithThisRootAtCenter = leftPathSum + rightPathSum - root.val;
        int greaterPath = Math.max(leftPathSum, rightPathSum);

        maxPath = Math.max(Math.max(pathWithThisRootAtCenter, Math.max(greaterPath, root.val)), maxPath);

        return Math.max(greaterPath, root.val);
    }
}