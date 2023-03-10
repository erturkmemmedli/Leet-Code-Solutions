class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int totalDuration = 0;
        for (int i = 0; i < timeSeries.length; i++) {
            if (i != timeSeries.length - 1) {
                if (timeSeries[i+1] - timeSeries[i] < duration) {
                    totalDuration += timeSeries[i+1] - timeSeries[i];
                } else {
                    totalDuration += duration;
                }
            } else {
                totalDuration += duration;
            }
        }
        return totalDuration;
    }
}
