class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        if (intervals.length == 0) {
            return new int[][] {newInterval};
        }

        List<int[]> result = new ArrayList<>();
        boolean added = false;

        if (newInterval[0] < intervals[0][0]) {
            result.add(newInterval);
            added = true;
        } else {
            result.add(intervals[0]);
        }

        int[] last;
        int[] curr;
        
        for (int i = 0; i < intervals.length; i++) {
            last = result.get(result.size() - 1);
            curr = intervals[i];

            if (curr[0] <= newInterval[0] && newInterval[0] <= curr[1]) {
                curr[1] = Math.max(curr[1], newInterval[1]);
                added = true;
            } else if (!added && newInterval[0] < curr[0]) {
                result.add(newInterval);
                added = true;
                last = result.get(result.size() - 1);
            }

            if (curr[0] <= last[1]) {
                result.set(result.size() - 1, new int[] {last[0], Math.max(last[1], curr[1])});
            } else {
                result.add(curr);
            }
        }

        if (newInterval[0] > result.get(result.size() - 1)[1]) {
            result.add(newInterval);
        }

        return result.toArray(new int[result.size()][2]);
    }
}

// Alternative solution

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        if (intervals.length == 0) {
            return new int[][] {newInterval};
        }

        List<int[]> result = new ArrayList<>();
        
        if (newInterval[1] < intervals[0][0]) {
            result.add(newInterval);
            for (int i = 0; i < intervals.length; i++) result.add(intervals[i]);
            return result.toArray(new int[result.size()][2]);
        }

        if (newInterval[0] > intervals[intervals.length - 1][1]) {
            for (int i = 0; i < intervals.length; i++) result.add(intervals[i]);
            result.add(newInterval);
            return result.toArray(new int[result.size()][2]);
        }

        Integer start = null;
        Integer end = null;
        int l = newInterval[0];
        int r = newInterval[1];
        
        for (int i = 0; i < intervals.length; i++) {
            if (l <= intervals[i][1] && start == null) {
                start = i;
            }
            if (r < intervals[i][0] && start != null) {
                end = i - 1;
                break;
            }
        }

        if (end == null) {
            intervals[intervals.length - 1][1] = Math.max(intervals[intervals.length - 1][1], r);
            end = intervals.length - 1;
        }

        for (int i = 0; i < start; i++) {
            result.add(intervals[i]);
        }

        result.add(new int[] {Math.min(intervals[start][0], l), Math.max(intervals[end][1], r)});

        for (int i = end + 1; i < intervals.length; i++) {
            result.add(intervals[i]);
        }

        return result.toArray(new int[result.size()][2]);
    }
}

// Alternative solution

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        int low = newInterval[0];
        int high = newInterval[1];
        int left = 0;
        int right = intervals.length - 1;

        int start = binarySearch(intervals, left, right, low, true);
        int end = binarySearch(intervals, left, right, high, false);
        
        for (int i = 0; i < start; i++) {
            result.add(intervals[i]);
        }

        if (start == end) {
            result.add(newInterval);
        } else {
            result.add(new int[] {Math.min(low, intervals[start][0]), Math.max(high, intervals[end - 1][1])});
        }
        
        for (int i = end; i < intervals.length; i++) {
            result.add(intervals[i]);
        }

        return result.toArray(new int[result.size()][2]);
    }

    public int binarySearch(int[][] intervals, int left, int right, int target, boolean isLeft) {
        if (left > right) {
            return left;
        }

        int mid = left + (right - left) / 2;

        if (intervals[mid][0] > target) {
            return binarySearch(intervals, left, mid - 1, target, isLeft);
        } else if (intervals[mid][1] < target) {
            return binarySearch(intervals, mid + 1, right, target, isLeft);
        } else {
            return (isLeft) ? mid : mid + 1;
        }
    }
}
