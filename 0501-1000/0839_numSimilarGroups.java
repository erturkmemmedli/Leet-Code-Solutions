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
    public int numSimilarGroups(String[] strs) {
        int n = strs.length;
        UnionFind uf = new UnionFind(n);
        HashSet<Integer> parents = new HashSet<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isSimilar(strs[i], strs[j])) {
                    uf.union(i, j);
                }
            }
        }
        for (int i = 0; i < n; i++) parents.add(uf.find(i));
        return parents.size();
    }

    public boolean isSimilar(String a, String b) {
        int count = 0;
        for (int i = 0; i < a.length(); i++) if (a.charAt(i) != b.charAt(i)) count++;
        return count <= 2;
    }
}
