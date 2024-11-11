class UnionFind {
    int[] parent;
    
    public UnionFind(int n) {
        this.parent = new int[n];
        for (int i = 0; i < n; i++) {
            this.parent[i] = i;
        }
    }

    public int find(int a) {
        while (a != this.parent[a]) {
            a = this.parent[a];
        }
        return a;
    }

    public boolean union(int a, int b) {
        int aRoot = find(a);
        int bRoot = find(b);
        if (aRoot == bRoot) {
            return false;
        }
        this.parent[bRoot] = aRoot;
        return true;
    }
}

class Solution {
    public int countComponents(int n, int[][] edges) {
        UnionFind uf = new UnionFind(n);
        HashSet<Integer> cc = new HashSet<>();

        for (int i = 0; i < edges.length; i++) {
            int a = edges[i][0];
            int b = edges[i][1];

            uf.union(a, b);
        }

        for (int i = 0; i < n; i++) {
            cc.add(uf.find(i));
        }

        return cc.size();
    }
}
