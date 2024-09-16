class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        HashMap<Integer, List<Integer>> graph = new HashMap<>();
        HashMap<Integer, Integer> indegree = new HashMap<>();
        Queue<Integer> queue = new LinkedList<>();
        List<Integer> toposort = new ArrayList<>();

        for (int i = 0; i < numCourses; i++) {
            graph.put(i, new ArrayList<>());
            indegree.put(i, 0);
        }

        for(int[] courses: prerequisites) {
            int a = courses[0];
            int b = courses[1];

            graph.get(b).add(a);
            indegree.put(a, indegree.get(a) + 1);            
        }

        for (Map.Entry<Integer, Integer> entry: indegree.entrySet()) {
            int key = entry.getKey();
            int val = entry.getValue();

            if (val == 0) {
                queue.add(key);
            }
        }

        while (!queue.isEmpty()) {
            int node = queue.remove();

            if (indegree.get(node) == 0) {
                toposort.add(node);
            }

            for (int child: graph.get(node)) {
                indegree.put(child, indegree.get(child) - 1);

                if (indegree.get(child) == 0) {
                    queue.add(child);
                }
            }
        }

        return toposort.size() == numCourses;
    }
}
