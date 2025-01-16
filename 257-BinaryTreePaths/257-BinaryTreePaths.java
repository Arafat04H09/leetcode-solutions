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
    ArrayList<String> ans = new ArrayList();
    public List<String> binaryTreePaths(TreeNode root) {
        if (root != null) {
            dfs(root, new StringBuilder(""));
        }
        return ans;
    }

    public void dfs(TreeNode root, StringBuilder sb) {
        if (root == null) {
            return;
        }

        int length = sb.length();

        if (length > 0) {
            sb.append("->");
        }
        sb.append(root.val);

        if (root.left == null && root.right == null) {
            ans.add(sb.toString());
        } else {
            dfs(root.left, sb);
            dfs(root.right, sb);
        }

        sb.setLength(length);
    }
}