/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int length = mountainArr.length();
        int low = 0; int high = length - 1; int peek = -1;
        int mid; int prev; int curr; int next;

        while (low <= high) {
            mid = low + (high - low) / 2;

            prev = mountainArr.get(mid - 1);
            curr = mountainArr.get(mid);
            next = mountainArr.get(mid + 1);

            if (curr > prev && curr > next) {
                peek = mid;
                break;
            } else if (prev < curr && curr < next) {
                low = mid;
            } else {
                high = mid;
            }
        }

        int result = -1;

        result = binarySearch(mountainArr, target, 0, peek, true);

        if (result != -1) {
            return result;
        }

        result = binarySearch(mountainArr, target, peek, length - 1, false);

        return result;
    }

    public int binarySearch(MountainArray mountainArr, int target, int low, int high, boolean increase) {
        int val; int mid;

        while (low <= high) {
            mid = low + (high - low) / 2;
            val = mountainArr.get(mid);

            if (val == target) {
                return mid;
            } else if ((val < target && increase) || (val > target && !increase)) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return -1;
    }
}
