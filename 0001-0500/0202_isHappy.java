class Solution {
    public boolean isHappy(int n) {
        int fast = n;
        int slow = n;

        while (fast != 1) {
            slow = convertNumber(slow);
            fast = convertNumber(convertNumber(fast));
            if (fast != 1 && slow == fast) {
                return false;
            }
        }

        return true;
    }

    public int convertNumber(int n) {
        int result = 0;

        while (n > 0) {
            int mod = n % 10;
            result += Math.pow(mod, 2);
            n /= 10;
        }

        return result;
    }
}
