class Solution {
    public boolean isValid(String word) {
        HashSet<Character> vowels = new HashSet<>(Arrays.asList('a', 'i', 'o', 'u', 'e'));

        int vowelCount = 0;
        int digitCount = 0;
        int n = word.length();

        if (n < 3) {
            return false;
        }
        
        for (int i = 0; i < n; i++) {
            char ch = word.charAt(i);
            int a = (int) ch;
            if ((a < 48) || (a > 57 && a < 65) || (a > 90 && a < 97) || (a > 122)) {
                return false;
            }
            if (Character.isDigit(ch)) {
                digitCount++;
            }
            if (vowels.contains(Character.toLowerCase(ch))) {
                vowelCount++;
            }
        }

        if (vowelCount == 0 || vowelCount + digitCount == n) {
            return false;
        }

        return true;
    }
}
