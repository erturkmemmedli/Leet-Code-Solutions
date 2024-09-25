class Solution {
    public HashMap<Character, char[]> digitMap;

    public Solution() {
        digitMap = new HashMap<>();
        digitMap.put('2', new char[] {'a', 'b', 'c'});
        digitMap.put('3', new char[] {'d', 'e', 'f'});
        digitMap.put('4', new char[] {'g', 'h', 'i'});
        digitMap.put('5', new char[] {'j', 'k', 'l'});
        digitMap.put('6', new char[] {'m', 'n', 'o'});
        digitMap.put('7', new char[] {'p', 'q', 'r', 's'});
        digitMap.put('8', new char[] {'t', 'u', 'v'});
        digitMap.put('9', new char[] {'w', 'x', 'y', 'z'});
    }

    public List<String> letterCombinations(String digits) {
        if (digits == null || digits.isEmpty()) {
            return new ArrayList<>();
        }
        
        List<String> output = new ArrayList<>();
        backtrack(digits, output, new StringBuilder(), 0);
        return output;
    }

    public void backtrack(String digits, List<String> output, StringBuilder path, int index) {
        if (digits.length() == index) {
            output.add(path.toString());
            return;
        }

        for (char c: digitMap.get(digits.charAt(index))) {
            path.append(c);
            backtrack(digits, output, path, index + 1);
            path.deleteCharAt(path.length() - 1);
        }
    }
}
