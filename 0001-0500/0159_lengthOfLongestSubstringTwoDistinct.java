class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        HashMap<Character, Integer> hashmap = new HashMap<>();
        int start = 0;
        int longest = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            while (hashmap.size() == 2 && !hashmap.containsKey(c)) {
                hashmap.put(s.charAt(start), hashmap.get(s.charAt(start)) - 1);
                if (hashmap.get(s.charAt(start)) == 0) {
                    hashmap.remove(s.charAt(start));
                }
                start++;
            }
            
            hashmap.put(c, hashmap.getOrDefault(c, 0) + 1);
            longest = Math.max(longest, i - start + 1);
        }
        
        return longest;
    }
}
