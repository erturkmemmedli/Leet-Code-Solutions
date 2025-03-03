class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        int count = 0;

        for (int i = 0; i < arr1.length; i++) {
            boolean flag = false;

            for (int j = 0; j < arr2.length; j++) {
                int diff = Math.abs(arr1[i] - arr2[j]);
                if (diff <= d) {
                    flag = true;
                    break;
                }
            }

            if (!flag) {
                count++;
            }
        }

        return count;
    }
}
