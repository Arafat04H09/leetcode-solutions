class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {      
        int start = 0, end = 0;
        int minDiff = Integer.MAX_VALUE;
        int curDiff = 0;

        for (end = 0; end < k; end++) {
            curDiff += Math.abs(x - arr[end]);
        }

        minDiff = curDiff;
        int bestStart = 0;

        while (end < arr.length) {
            curDiff += Math.abs(x - arr[end]);
            curDiff -= Math.abs(x - arr[start]);

            if (curDiff < minDiff) {
                bestStart = start + 1; 
                minDiff = curDiff;
            }

            start++;
            end++;
        }

        List<Integer> result = new ArrayList<>();
        for (int i = bestStart; i < bestStart + k; i++) {
            result.add(arr[i]);
        }
        
        return result;
    }
}