class Solution {
    public int numberOfArrays(int[] differences, int lower, int upper) {
        long curr = lower;
        long max = curr;
        long min = curr;

        for (int num: differences) {
            curr += num;
            max = Math.max(max, curr);
            min = Math.min(min, curr);
        }

        long high = max + lower - min;

        return (int) Math.max(upper - high + 1, 0);
    }
}
