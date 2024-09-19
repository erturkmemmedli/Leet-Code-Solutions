class Solution {
    public List<Integer> output = new ArrayList<>();

    public List<Integer> lexicalOrder(int n) {
        recursiveTrie(0, n);
        return output;
    }

    public void recursiveTrie(int node, int n) {
        for (int i = node; i <= Math.min(node + 9, n); i++) {
            if (i == 0) continue;
            output.add(i);
            if (10 * i <= n) recursiveTrie(10 * i, n);
        }
    }
}
