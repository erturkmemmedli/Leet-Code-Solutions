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
            if (list.size() > 1) {
                maxRange = Math.max(maxRange, list.get(list.size() - 1) - list.get(0) - 1);
            }
        }

        return maxRange;
    }
}
