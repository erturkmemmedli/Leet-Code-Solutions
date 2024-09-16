class Tuple implements Comparable<Tuple> {
    private char letter;
    private int count;

    public Tuple(char letter, int count) {
        this.letter = letter;
        this.count = count;
    }

    public char getLetter() {
        return this.letter;
    }

    public int getCount() {
        return this.count;
    }

    @Override
    public int compareTo(Tuple tuple) {
        return this.count - tuple.count;
    }
}

class Solution {
    public String frequencySort(String s) {
        HashMap<Character, Integer> counter = new HashMap<>();
        PriorityQueue<Tuple> pQueue = new PriorityQueue<>();
        StringBuilder string = new StringBuilder();

        for (int c = 0; c < s.length(); c++) {
            counter.put(s.charAt(c), counter.getOrDefault(s.charAt(c), 0) + 1);
        }

        counter.forEach((key, val) -> pQueue.add(new Tuple(key, -val)));

        while (!pQueue.isEmpty()) {
            Tuple tuple = pQueue.poll();

            for (int i = 0; i < -tuple.getCount(); i++) {
                string.append(tuple.getLetter());
            }
        }

        return string.toString();
    }
}
