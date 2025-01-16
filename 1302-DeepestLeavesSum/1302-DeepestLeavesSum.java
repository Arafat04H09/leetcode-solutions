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
    public int deepestLeavesSum(TreeNode root) {
        if (root == null) { return 0; }

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int levelSum = 0;

        while (!q.isEmpty()) {
            levelSum = 0;

            int levelSize = q.size();

            for (int i = 0; i < levelSize; i++) {
                TreeNode currentNode = q.poll();
                levelSum += currentNode.val;

                if (currentNode.left != null) {
                    q.add(currentNode.left);
                }
                if (currentNode.right != null) {
                    q.add(currentNode.right);
                }
            }
        }
        
        return levelSum;
    }
}