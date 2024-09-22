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

    public void union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return;
        if (this.rank[ra] > this.rank[rb]) this.parent[rb] = ra;
        else if (this.rank[ra] < this.rank[rb]) this.parent[ra] = rb;
        else {this.parent[rb] = ra; this.rank[ra]++;}
    }
}

class Solution {
    public int makeConnected(int n, int[][] connections) {
        int l = connections.length;
        if (l < n - 1) return -1;
        UnionFind uf = new UnionFind(n);
        HashSet parents = new HashSet<>();
        for (int i = 0; i < l; i++) uf.union(connections[i][0], connections[i][1]);
        for (int i = 0; i < n; i++) parents.add(uf.find(i));
        return parents.size() - 1;
    }
}
