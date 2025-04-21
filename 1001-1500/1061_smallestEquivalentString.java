class UnionFind {
    public int[] parent = new int[26];

    public UnionFind() {
        for (int i = 0; i < 26; i++) {
            this.parent[i] = i;
        }
    }

    public int find(int node) {
        while (node != this.parent[node]) {
            node = this.parent[node];
        }
        return node;
    }

    public void union(int node1, int node2) {
        int parent1 = find(node1);
        int parent2 = find(node2);
        
        if (parent1 != parent2) {
            if (parent1 > parent2) {
                this.parent[parent1] = parent2;
            } else {
                this.parent[parent2] = parent1;
            }
        }
    }
}


class Solution {
    public String smallestEquivalentString(String s1, String s2, String baseStr) {
        UnionFind uf = new UnionFind();

        for (int i = 0; i < s1.length(); i++) {
            uf.union((int) s1.charAt(i) - 97, (int) s2.charAt(i) - 97);
        }

        StringBuilder resultString = new StringBuilder();

        for (int i = 0; i < baseStr.length(); i++) {
            resultString.append((char) (97 + uf.find((int) baseStr.charAt(i) - 97)));
        }

        return resultString.toString();
    }
}
