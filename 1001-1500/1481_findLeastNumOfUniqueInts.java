class Tuple implements Comparable<Tuple> {
    private int key;
    private int value;

    public Tuple(int key, int value) {
        this.key = key;
        this.value = value;
    }

    @Override
    public int compareTo(Tuple tuple) {
        return this.value - tuple.value;
    }

    public int getKey() {
        return this.key;
    }

    public int getValue() {
        return this.value;
    }
}

class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        PriorityQueue<Tuple> pq = new PriorityQueue<>();
        int uniqueNumbers = 0;

        for (int num: arr) counter.put(num, counter.getOrDefault(num, 0) + 1);

        for (Map.Entry<Integer, Integer> entry: counter.entrySet()) {
            int key = entry.getKey();
            int value = entry.getValue();
            pq.add(new Tuple(key, value));
        }

        while (k >= 0 && !pq.isEmpty()) {
            Tuple tuple = pq.poll();
            if (k - tuple.getValue() >= 0) uniqueNumbers++;
            k -= tuple.getValue();
        }

        return counter.size() - uniqueNumbers;
    }
}
