class Solution {
    public int countWords(String[] words1, String[] words2) {
        HashMap<String, int[]> map = new HashMap<>();
        int count = 0;

        for (String word: words1) {
            if (!map.containsKey(word)) {
                map.put(word, new int[2]);
            }
            int[] values = map.get(word);
            values[0] += 1;
            map.put(word, values);
        }

        for (String word: words2) {
            if (!map.containsKey(word)) {
                map.put(word, new int[2]);
            }
            int[] values = map.get(word);
            values[1] += 1;
            map.put(word, values);
        }

        
        for (Map.Entry<String, int[]> entry : map.entrySet()) {
            String key = entry.getKey();
            int[] value = entry.getValue();

            if (value[0] == 1 && value[1] == 1) {
                count++;
            }
        }

        return count;
    }
}
