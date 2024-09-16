class Solution {
    public int[] frequencySort(int[] nums) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        PriorityQueue<int[]> pQueue = new PriorityQueue<>((a, b) -> {
            if (a[1] != b[1]) return a[1] - b[1];
            else return b[0] - a[0];
        });

        for (int num: nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        counter.forEach((num, count) -> pQueue.add(new int[]{num, count}));

        int i = 0;

        while (!pQueue.isEmpty()) {
            int[] pair = pQueue.poll();

            for (int j = 0; j < pair[1]; j++) {
                nums[i] = pair[0];
                i++;
            }
        }

        return nums;
    }
}

// Alternative solution

class Tuple implements Comparator<Tuple> {
    private int number;
    private int count;

    public Tuple(int number, int count) {
        this.number = number;
        this.count = count;
    }

    public int getNumber() {
        return this.number;
    }

    public int getCount() {
        return this.count;
    }

    @Override
    public int compare(Tuple o1, Tuple o2) {
        if (o1.count > o2.count || o1.count < o2.count) {
            return o1.count - o2.count;
        } else {
            return o2.number - o1.number;
        }
    }
}

class Solution {
    public int[] frequencySort(int[] nums) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        PriorityQueue<Tuple> pQueue = new PriorityQueue<>(new Tuple (Integer.MAX_VALUE, Integer.MIN_VALUE));

        for (int num: nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry: counter.entrySet()) {
            Integer number = entry.getKey();
            Integer count = entry.getValue();

            pQueue.add(new Tuple(number, count));
        }

        int i = 0;

        while (!pQueue.isEmpty()) {
            Tuple tuple = pQueue.poll();

            for (int j = 0; j < tuple.getCount(); j++) {
                nums[i] = tuple.getNumber();
                i++;
            }
        }

        return nums;
    }
}
