class Solution {
    public List<Integer> mostVisited(int n, int[] rounds) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        int current = rounds[0];
        hashmap.put(current, 1);
        int i = 1;

        while (i < rounds.length) {
            current = current % n + 1;
            hashmap.put(current, hashmap.getOrDefault(current, 0) + 1);

            if (current == rounds[i]) {
                i++;
            }
        }

        int max = 0;

        for (Map.Entry<Integer, Integer> entry: hashmap.entrySet()) {
            max = Math.max(max, entry.getValue());
        }

        List<Integer> output = new ArrayList<>();

        for (Map.Entry<Integer, Integer> entry: hashmap.entrySet()) {
            if (entry.getValue() == max) {
                output.add(entry.getKey());
            }
        }

        Collections.sort(output);
        return output;
    }
}
