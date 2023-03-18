class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        HashMap<Integer, List<Integer>> graph = new HashMap<Integer, List<Integer>>();
        HashSet<Integer> visited = new HashSet<Integer>(); 

        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList());
        }

        for (int[] edge: edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        return dfs(graph, visited, source, destination);
    }

    public static boolean dfs(HashMap<Integer, List<Integer>> graph, HashSet<Integer> visited, int source, int destination) {
        if (source == destination) {
            return true;
        }

        if (visited.contains(source) || graph.get(source) == null) {
            return false;
        }
        
        visited.add(source);

        for (int neighbor: graph.get(source)) {
            if (dfs(graph, visited, neighbor, destination)) {
                return true;
            }
        }

        return false;
    }
}
