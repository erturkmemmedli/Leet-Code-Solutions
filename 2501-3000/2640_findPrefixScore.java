class Solution {
    public long[] findPrefixScore(int[] nums) {
        ArrayList<Long> prefixScores = new ArrayList<>();
        int max = 0;
        int sum = 0;

        for (int num : nums) {
            if (num > max) {
                max = num;
            }
            long current = num + max;
            prefixScores.add(current);
        }

        for (int i = 1; i < prefixScores.size(); i++) {
            prefixScores.set(i, prefixScores.get(i) + prefixScores.get(i - 1));
        }

        long[] result = prefixScores.stream().mapToLong(Long::longValue).toArray();

        return result;
    }
}
