class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        HashMap<Character, List<Integer>> map = new HashMap<>();
        int maxRange = -1;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!map.containsKey(c)) {
                map.put(c, new ArrayList<>());
            }
            map.get(c).add(i);
        }

        for (Map.Entry<Character, List<Integer>> entry: map.entrySet()) {
            List<Integer> list = entry.getValue();
            for (int i = 1; i < list.size(); i++) {
                maxRange = Math.max(maxRange, list.get(i) - list.get(i - 1) - 1);
            }
        }

        return maxRange;
    }
}
