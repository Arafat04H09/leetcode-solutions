class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> prefixSum = new HashMap<>();
        prefixSum.put(0, 1);
        int count = 0;
        int curSum = 0;

        for (int num: nums) {
            curSum += num;

            count += prefixSum.getOrDefault(curSum - k, 0);

            prefixSum.put(curSum, prefixSum.getOrDefault(curSum, 0) + 1);
        }

        return count;
    }
}