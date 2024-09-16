class Solution {
    public int totalFruit(int[] fruits) {
        HashMap<Integer, Integer> window = new HashMap<>();
        int start = 0;
        int total = 0;

        for (int end = 0; end < fruits.length; end++) {
            while (window.size() == 2 && !window.containsKey(fruits[end])) {
                window.put(fruits[start], window.get(fruits[start]) - 1);

                if (window.get(fruits[start]) == 0) {
                    window.remove(fruits[start]);
                }
                start++;
            }

            window.put(fruits[end], window.getOrDefault(fruits[end], 0) + 1);
            total = Math.max(total, end - start + 1);
        }

        return total;
    }
}
