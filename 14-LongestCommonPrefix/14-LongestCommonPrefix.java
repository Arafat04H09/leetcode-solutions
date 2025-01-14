class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0 || strs == null) {
            return "";
        }

        Arrays.sort(strs);
        char[] firstWord = strs[0].toCharArray();
        char[] lastWord = strs[strs.length - 1].toCharArray();
        StringBuilder prefix = new StringBuilder();
        int idx = 0;

        while (idx < firstWord.length && firstWord[idx] == lastWord[idx]) {
            prefix.append(firstWord[idx]);
            idx++;
        }

        return prefix.toString(); 
    }
}