class Solution {
    public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        Arrays.sort(slots1, (a, b) -> Integer.compare(a[0], b[0]));
        Arrays.sort(slots2, (a, b) -> Integer.compare(a[0], b[0]));
        
        int i = 0;
        int j = 0;
        
        while (i < slots1.length && j < slots2.length) {
            int left = Math.max(slots1[i][0], slots2[j][0]);
            
            if (slots1[i][1] < slots2[j][1]) {
                int right = slots1[i][1];
                if (right - left >= duration) {
                    return List.of(left, left + duration);
                }
                i++;
            } else if (slots1[i][1] > slots2[j][1]) {
                int right = slots2[j][1];
                if (right - left >= duration) {
                    return List.of(left, left + duration);
                }
                j++;
            } else {
                int right = slots2[j][1];
                if (right - left >= duration) {
                    return List.of(left, left + duration);
                }
                i++;
                j++;
            }
        }
        
        return new ArrayList<>();
    }
}
