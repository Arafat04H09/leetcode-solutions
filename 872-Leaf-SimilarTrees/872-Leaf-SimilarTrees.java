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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> leaves1 = new ArrayList();
        ArrayList<Integer> leaves2 = new ArrayList();

        getLeaves(root1, leaves1);
        getLeaves(root2, leaves2);

        return leaves1.equals(leaves2);
    }

    public void getLeaves(TreeNode node, ArrayList<Integer> list) {
        if (node != null) {
            if (node.left == null  && node.right == null) {
                list.add(node.val);
            }
            getLeaves(node.left, list);
            getLeaves(node.right, list);
        }
    }
}