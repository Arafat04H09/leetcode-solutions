class Solution {
    public String countAndSay(int n) {
        String s = "1";

        for (int i = 1; i < n; i++) {
            s = nextString(s);
        }

        return s;
    }

    public String nextString(String s) {
        StringBuilder sb = new StringBuilder();

        char[] arr = s.toCharArray();
        int count = 1;
        char prev = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == prev) {
                count += 1;
            } else {
                sb.append(String.valueOf(count));
                sb.append(String.valueOf(prev));
                prev = arr[i];
                count = 1;
            }
        }
        sb.append(String.valueOf(count));
        sb.append(String.valueOf(prev));

        return sb.toString();
    }
}