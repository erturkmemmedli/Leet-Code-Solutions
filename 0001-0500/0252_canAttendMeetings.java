class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        if (intervals.length == 0) {
            return true;
        }

        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        int[] last = intervals[0];
        int[] curr;
        
        for (int i = 1; i < intervals.length; i++) {
            curr = intervals[i];
            
            if (last[1] > curr[0]) {
                return false;
            } else {
                last = curr;
            }
        }
        
        return true;
    }
}
