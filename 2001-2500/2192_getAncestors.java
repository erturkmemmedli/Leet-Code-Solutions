class Solution {
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        ArrayList<Integer>[] graph = new ArrayList[n];
        int[] indegree = new int[n];
        List<HashSet<Integer>> ancestors = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
            ancestors.add(new HashSet<>());
        }

        for (int[] edge: edges) {
            int from = edge[0];
            int to = edge[1];

            graph[from].add(to);
            indegree[to]++;
        }

        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                queue.add(i);
            }
        }

        while (!queue.isEmpty()) {
            int length = queue.size();

            for (int i = 0; i < length; i++) {
                int node = queue.remove();

                for (int child: graph[node]) {
                    indegree[child]--;
                    ancestors.get(child).add(node);

                    for (int kid: ancestors.get(node)) {
                        ancestors.get(child).add(kid);
                    }

                    if (indegree[child] == 0) {
                        queue.add(child);
                    }
                }
            }
        }

        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            List<Integer> ancestor = new ArrayList<>(ancestors.get(i));
            Collections.sort(ancestor);
            result.add(ancestor);
        }

        return result;
    }
}
