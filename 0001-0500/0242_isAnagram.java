class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        HashMap<Character, Integer> map = new HashMap<>();
        for (int i=0; i<s.length(); i++) {
            char c1 = s.charAt(i);
            map.put(c1, map.getOrDefault(c1, 0) + 1);
        }

        for (int i=0; i<t.length(); i++) {
            char c2 = t.charAt(i);
            if (!map.containsKey(c2)) return false;
            map.put(c2, map.get(c2) - 1);
            if (map.get(c2) == 0) map.remove(c2);
        }

        return map.isEmpty();
    }
}
