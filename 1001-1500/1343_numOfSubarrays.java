class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int count = 0;
        double windowSum = 0;
        for (int i=0; i<k; i++) windowSum += arr[i];
        double average = windowSum / k;
        if (average >= threshold) count++;
        for (int i=k; i<arr.length; i++) {
            windowSum += arr[i] - arr[i-k];
            average = windowSum / k;
            if (average >= threshold) count++;
        }
        return count;
    }
}
