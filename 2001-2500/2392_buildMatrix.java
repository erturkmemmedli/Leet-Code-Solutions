class Solution {
    public int[][] buildMatrix(int k, int[][] rowConditions, int[][] colConditions) {
        int[][] coordinates = new int[k][2];
        int[][] matrix = new int[k][k];
        List<Integer> toposortedRow = toposort(k, rowConditions);
        List<Integer> toposortedCol = toposort(k, colConditions);

        if (toposortedRow.size() != k || toposortedCol.size() != k) {
            return new int[0][0];
        }

        for (int i = 0; i < k; i++) {
            int rowVal = toposortedRow.get(i);
            int colVal = toposortedCol.get(i);

            coordinates[rowVal][0] = i;
            coordinates[colVal][1] = i;
        }

        for (int i = 0; i < k; i++) {
            int[] coordinate = coordinates[i];
            int r = coordinate[0];
            int c = coordinate[1];

            matrix[r][c] = i + 1;
        }

        return matrix;
    }

    public List<Integer> toposort(int k, int[][] conditions) {
        ArrayList<Integer>[] graph = new ArrayList[k];
        int[] indegree = new int[k];
        Queue<Integer> queue = new LinkedList<>();
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < k; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] condition: conditions) {
            int u = condition[0] - 1, v = condition[1] - 1;
            graph[u].add(v);
            indegree[v]++;
        }

        for (int i = 0; i < k; i++) {
            if (indegree[i] == 0) {
                queue.add(i);
            }
        }

        while (!queue.isEmpty()) {
            int node = queue.remove();
            result.add(node);

            for (int child: graph[node]) {
                indegree[child]--;

                if (indegree[child] == 0) {
                    queue.add(child);
                }
            }
        }

        return result;
    }
}
