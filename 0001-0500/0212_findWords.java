class Node {
    HashMap<Character, Node> children;
    boolean isEnd;

    public Node() {
        this.children = new HashMap<>();
        this.isEnd = false;
    }
}

class Trie {
    Node root;

    public Trie() {
        this.root = new Node();
    }

    public void insert(String word) {
        Node node = this.root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (!node.children.containsKey(c)) {
                node.children.put(c, new Node());
            }
            node = node.children.get(c);
        }
        node.isEnd = true;
    }
}

class Solution {
    public int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

    public List<String> findWords(char[][] board, String[] words) {
        int m = board.length, n = board[0].length;
        Trie trie = new Trie();
        List<String> output = new ArrayList<>();
        HashSet<String> visited;

        for (String word: words) {
            trie.insert(word);
        }

        Node root = trie.root;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = board[i][j];
                if (root.children.containsKey(c)) {
                    String path = "" + c;
                    visited = new HashSet<>();
                    visited.add(i + "," + j);
                    dfs(board, output, root.children.get(c), visited, m, n, i, j, path);
                }
            }
        }

        return output;
    }

    public void dfs(char[][] b, List<String> o, Node node, HashSet<String> v, int m, int n, int i, int j, String p) {
        if (node.isEnd) {
            node.isEnd = false;
            o.add(p);
        }

        for (int[] dir: directions) {
            int x = i + dir[0], y = j + dir[1];
            if (x >= 0 && x < m && y >= 0 && y < n && node.children.containsKey(b[x][y]) && !v.contains(x + "," + y)) {
                v.add(x + "," + y);
                dfs(b, o, node.children.get(b[x][y]), v, m, n, x, y, p + b[x][y]);
                v.remove(x + "," + y);
            }
        }
    }
}
