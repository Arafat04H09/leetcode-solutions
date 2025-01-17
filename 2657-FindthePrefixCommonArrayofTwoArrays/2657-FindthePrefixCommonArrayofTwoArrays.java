public int[]ThePrefixCommonArray(int[] A, int[] B) {
    int length = A.length;
    // Create two hash maps to store the indices of each element in A and B
    HashMap<Integer, Integer> indexStoreOfA = new HashMap<>();
    HashMap<Integer, Integer> indexStoreOfB = new HashMap<>();
    // Populate the hash maps with the indices of each element in A and B
    for (int i = 0; i < length; i++) {
        indexStoreOfA.put(A[i], i);
        indexStoreOfB.put(B[i], i);
    }
    // Create an array to store the prefix common array
    int[] answer = new int[length];
    // Iterate over each element in A
    for (int i = 0; i < length; i++) {
        int prefixCounter = 0;
        // Iterate over each element in the prefix of A up to i
        for (int j = 0; j <= i; j++) {
            // If the element at index j in A is also in B and its index in both A and B is less than or equal to i,
            // increment the prefix counter
            if (indexStoreOfA.get(A[j]) <= i && indexStoreOfB.get(A[j]) <= i) prefixCounter++;
        }
        // Store the prefix counter in the answer array
        answer[i] = prefixCounter;
    }
    // Return the prefix common array
    return answer;
}