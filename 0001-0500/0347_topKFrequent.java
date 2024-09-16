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
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> counterMap = new HashMap<>();
        PriorityQueue<Tuple> pQueue = new PriorityQueue<>();
        int[] resultSet = new int[k];
        
        for(int num: nums) {
            counterMap.put(num, counterMap.getOrDefault(num, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry: counterMap.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();

            if (pQueue.size() < k) {
                pQueue.add(new Tuple(key, value));
                continue;
            }

            if (pQueue.peek().getValue() < value) {
                pQueue.poll();
                pQueue.add(new Tuple(key, value));
            }
        }

        int i = 0;

        for (Tuple tuple: pQueue) {
            resultSet[i] = tuple.getKey();
            i++;
        }

        return resultSet;
    }
}
