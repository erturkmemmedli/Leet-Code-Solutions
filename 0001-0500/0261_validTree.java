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
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n-1) {
            return false;
        }
        
        UnionFind uf = new UnionFind(n);
        for (int i = 0; i < edges.length; i++) {
            if (!uf.union(edges[i][0], edges[i][1])) {
                return false;
            }
        }
        
        return true;
    }
}
