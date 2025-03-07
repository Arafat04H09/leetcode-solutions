class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int l = 0, r = people.length - 1;
        int boats = 0;

        while (l <= r) {
            if (people [l] + people[r] <= limit) {
                l+= 1;
            }
            r-= 1;
            boats += 1;
        }

        return boats;
    }
}