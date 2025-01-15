    // O(max(M,N)) time. Terminate early if nums2 reach end.
    // Otherwise, pick nums2 if nums1 reach end or nums2 is larger.
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int i = m - 1, j = n - 1, k = m + n - 1; k >= 0 && j >= 0; k--)
            nums1[k] = (i < 0 || nums1[i] < nums2[j]) ? nums2[j--] : nums1[i--];
    }