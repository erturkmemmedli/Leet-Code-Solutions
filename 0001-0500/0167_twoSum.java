class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int x = 0;
        int y = numbers.length - 1;

        while (true) {
            if (numbers[x] + numbers[y] == target) {
                return new int[] {x+1, y+1};
            } else if (numbers[x] + numbers[y] > target) {
                y -= 1;
            } else {
                x += 1;
            }
        }
    }
}
