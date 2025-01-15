class Solution {
    public String mergeAlternately(String word1, String word2) {
        int idx1 = 0, idx2 = 0, len1 = word1.length(), len2 = word2.length();
        StringBuilder sb = new StringBuilder();

        while (idx1 < len1 && idx2 < len2) {
            sb.append(word1.charAt(idx1++));
            sb.append(word2.charAt(idx2++));
        }

        while (idx1 < len1) {
            sb.append(word1.charAt(idx1++));
        }

        while (idx2 < len2) {
            sb.append(word2.charAt(idx2++));
        }

        return sb.toString();
    }
}