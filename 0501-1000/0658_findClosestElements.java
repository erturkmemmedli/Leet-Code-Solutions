class Tuple implements Comparator<Tuple> {
    private int val;
    private int distance;

    public Tuple(int val, int distance) {
        this.val = val;
        this.distance = distance;
    }

    public int getVal() {
        return this.val;
    }

    public int getDistance() {
        return this.distance;
    }

    @Override
    public int compare(Tuple o1, Tuple o2) {
        if (o1.distance != o2.distance) {
            return o1.distance - o2.distance;
        } else {
            return o1.val - o2.val;
        }
    }
}

class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        PriorityQueue<Tuple> pq = new PriorityQueue<>(new Tuple(0, 0));
        List<Integer> result = new ArrayList<>();

        for (int num: arr) {
            int distance = Math.abs(num - x);

            if (pq.size() < k) {
                pq.add(new Tuple(num, -distance));
                continue;
            }

            if (-pq.peek().getDistance() > distance) {
                pq.poll();
                pq.add(new Tuple(num, -distance));
            }
        }

        while (!pq.isEmpty()) {
            result.add(pq.poll().getVal());
        }

        Collections.sort(result);
        return result;
    }
}
