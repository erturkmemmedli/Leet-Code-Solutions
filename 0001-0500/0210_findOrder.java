class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        ArrayList<Integer>[] graph = new ArrayList[numCourses];
        int[] indegree = new int[numCourses];
        Queue<Integer> queue = new LinkedList<>();
        List<Integer> toposort = new ArrayList<>();

        for (int i = 0; i < numCourses; i++) graph[i] = new ArrayList<>();

        for(int[] e: prerequisites) {
            graph[e[1]].add(e[0]);
            indegree[e[0]]++;            
        }

        for (int i = 0; i < numCourses; i++) if (indegree[i] == 0) queue.add(i);

        while (!queue.isEmpty()) {
            int node = queue.remove();
            if (indegree[node] == 0) toposort.add(node);

            for (int child: graph[node]) {
                indegree[child]--;
                if (indegree[child] == 0) queue.add(child);
            }
        }

        return (toposort.size() != numCourses) ? new int[] {} : toposort.stream().mapToInt(i -> i).toArray();
    }
}
