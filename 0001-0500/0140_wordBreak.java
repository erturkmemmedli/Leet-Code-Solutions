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

            if(!node.children.containsKey(c)) {
                node.children.put(c, new Node());
            }

            node = node.children.get(c);
        }

        node.isEnd = true;
    }

    public List<String[]> search(String str) {
        Node node = this.root;
        List<String[]> nextStrings = new ArrayList<>();

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);

            if (!node.children.containsKey(c)) {
                return nextStrings;
            }

            node = node.children.get(c);

            if (node.isEnd) {
                nextStrings.add(new String[] {str.substring(0, i + 1), str.substring(i + 1)});
            }
        }

        return nextStrings;
    }
}

class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Trie trie = new Trie();
        List<String> output = new ArrayList<>();

        for (String word: wordDict) {
            trie.insert(word);
        }

        dfs(s, trie, output, "");
        return output;
    }

    public void dfs(String str, Trie trie, List<String> output, String current) {
        if (str.length() == 0) {
            output.add(current);
            return;
        }

        List<String[]> nextStrings = trie.search(str);

        for (String[] stringPair: nextStrings) {
            String head = stringPair[0];
            String searchable = stringPair[1];
            
            String newCurrent = current + ((current.length() == 0) ? head : " " + head);
            dfs(searchable, trie, output, newCurrent);
        }

        return;
    }
}
