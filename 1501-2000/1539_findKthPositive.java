class Solution {
    public int findKthPositive(int[] arr, int k) {
        return binarySearch(arr, k, 0, 0, arr.length - 1);
    }

    public int binarySearch(int[] arr, int k, int base, int start, int end) {
        if (end < start) {
            return (end >= 0) ? arr[end] + k : k;
        }

        int mid = start + (end - start) / 2;
        int num = arr[mid];
        int count = num - base - (mid - start + 1);
        int newK = k - count;

        if (newK > 0) {
            return binarySearch(arr, newK, arr[mid], mid + 1, end);
        } else {
            return binarySearch(arr, k, base, start, end - 1);
        }
    }
}
