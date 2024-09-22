class UnionFind {
    int[] parent;
    int[] rank;

    public UnionFind(int n) {
        this.parent = new int[n];
        this.rank = new int[n];
        for (int i = 0; i < n; i++) this.parent[i] = i;
    }

    public int find(int a) {
        while (a != this.parent[a]) a = this.parent[a];
        return a;
    }

    public boolean union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false;
        if (this.rank[rb] < this.rank[ra]) this.parent[rb] = ra;
        else if (this.rank[rb] > this.rank[ra]) this.parent[ra] = rb;
        else {this.parent[rb] = ra; this.rank[ra]++;}
        return true;
    }
}

class Solution {
    public int maxNumEdgesToRemove(int n, int[][] edges) {
        HashMap<Integer, List<Integer>> traverseMap = new HashMap<>();
        traverseMap.put(1, new ArrayList<>());
        traverseMap.put(2, new ArrayList<>());
        traverseMap.put(3, new ArrayList<>());

        UnionFind ufAlice = new UnionFind(n);
        UnionFind ufBob = new UnionFind(n);
        HashSet<Integer> parentAlice = new HashSet<>();
        HashSet<Integer> parentBob = new HashSet<>();
        int redundant = 0;

        for (int i = 0; i < edges.length; i++) {
            traverseMap.get(edges[i][0]).add(i);
        }

        for (int node: traverseMap.get(3)) {
            if (!ufAlice.union(edges[node][1] - 1, edges[node][2] - 1)) redundant++;
            ufBob.union(edges[node][1] - 1, edges[node][2] - 1);
        }

        for (int node: traverseMap.get(1)) {
            if (!ufAlice.union(edges[node][1] - 1, edges[node][2] - 1)) redundant++;
        }

        for (int node: traverseMap.get(2)) {
            if (!ufBob.union(edges[node][1] - 1, edges[node][2] - 1)) redundant++;
        }

        for (int i = 0; i < n; i++) parentAlice.add(ufAlice.find(i));
        for (int i = 0; i < n; i++) parentBob.add(ufBob.find(i));

        if (parentAlice.size() != 1 || parentBob.size() != 1) return -1;
        return redundant;
    }
}
