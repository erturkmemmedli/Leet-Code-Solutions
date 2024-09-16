class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        ArrayList<Integer>[] graph = new ArrayList[n];
        int[] indegree = new int[n];
        Queue<Integer> queue = new LinkedList<>();
        int remaining = n;

        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] edge: edges) {
            int u = edge[0];
            int v = edge[1];
            graph[u].add(v);
            graph[v].add(u);
            indegree[u]++;
            indegree[v]++;
        }

        for (int i = 0; i < n; i++) {
            if (indegree[i] <= 1) {
                queue.add(i);
            }
        }
        
        while (remaining > 2) {
            int length = queue.size();

            for (int i = 0; i < length; i++) {
                int node = queue.remove();
                remaining--;

                for (int child: graph[node]) {
                    indegree[child]--;

                    if (indegree[child] == 1) {
                        queue.add(child);
                    }
                }
            }
        }

        return new ArrayList(queue);
    }
}
