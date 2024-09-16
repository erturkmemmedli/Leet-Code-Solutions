class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));
        List<int[]> result = new ArrayList<>();
        result.add(intervals[0]);
        int[] last;
        int[] curr;

        for (int i = 1; i < intervals.length; i++) {
            last = result.get(result.size() - 1);
            curr = intervals[i];

            if (curr[0] <= last[1]) {
                result.set(result.size() - 1, new int[] {last[0], Math.max(last[1], curr[1])});
            } else {
                result.add(curr);
            }
        }

        return result.toArray(new int[result.size()][2]);
    }
}
