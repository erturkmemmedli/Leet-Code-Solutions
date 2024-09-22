class UnionFind {
    int[] parent;
    int[] rank;

    public UnionFind(int n) {
        this.parent = new int[n];
        this.rank = new int[n];

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

    public void union(int a, int b) {
        int aRoot = find(a);
        int bRoot = find(b);

        if (aRoot != bRoot) {
            if (this.rank[bRoot] < this.rank[aRoot]) {
                this.parent[bRoot] = aRoot;
            } else if (this.rank[bRoot] == this.rank[aRoot]) {
                this.parent[bRoot] = aRoot;
                this.rank[aRoot]++;
            } else {
                this.parent[aRoot] = bRoot;
            }
        }
    }
}

class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        UnionFind unionFind = new UnionFind(n);
        HashSet<Integer> parentSet = new HashSet<>();

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) {
                     unionFind.union(i, j);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            parentSet.add(unionFind.find(i));
        }

        return parentSet.size();
    }
}
