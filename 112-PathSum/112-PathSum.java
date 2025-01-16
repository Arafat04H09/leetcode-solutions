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
    private boolean found = false;

    public boolean hasPathSum(TreeNode root, int targetSum) {
        sumHelper(root, targetSum, 0);
        return found;
    }

    public void sumHelper(TreeNode root, int targetSum, int curSum) {
        if (root == null) {
            return;
        }

        curSum += root.val;

        if (root.left == null && root.right == null) {
            if (curSum == targetSum) {
                found = true;
            }
        } else {
            sumHelper(root.left, targetSum, curSum);
            sumHelper(root.right, targetSum, curSum);
        }

        curSum -= root.val;
    }
}