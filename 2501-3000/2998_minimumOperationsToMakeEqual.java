class Solution {

    public int minimumOperationsToMakeEqual(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        HashSet<Integer> set = new HashSet<>();

        queue.add(new int[] {y, 0});

        while (!queue.isEmpty()) {
            int[] pair = queue.remove();
            int node = pair[0], distance = pair[1];

            if (node == x) {
                return distance;
            }

            if (node + 1 <= Math.min(x + 11, 10000) && !set.contains(node + 1)) {
                queue.add(new int[] {node + 1, distance + 1});
                set.add(node + 1);
            }
            if (node - 1 >= 1 && !set.contains(node - 1)) {
                queue.add(new int[] {node - 1, distance + 1});
                set.add(node - 1);
            }
            if (node * 11 <= Math.min(x + 11, 10000) && !set.contains(node * 11)) {
                queue.add(new int[] {node * 11, distance + 1});
                set.add(node * 11);
            }
            if (node * 5 <= Math.min(x + 11, 10000) && !set.contains(node * 5)) {
                queue.add(new int[] {node * 5, distance + 1});
                set.add(node * 5);
            }
        }
        return -1;
    }
}
