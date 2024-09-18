class TrieNode {
    HashMap<Character, TrieNode> children;
    boolean isEnd;

    public TrieNode() {
        this.children = new HashMap<>();
        this.isEnd = false;
    }
}

class Trie {
    TrieNode root;

    public Trie() {
        this.root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode node = this.root;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);

            if (!node.children.containsKey(c)) {
                node.children.put(c, new TrieNode());
            }

            node = node.children.get(c);
        }

        node.isEnd = true;
    }

    public String search(String word) {
        TrieNode node = this.root;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);

            if (node.isEnd) {
                return word.substring(0, i);
            }

            if (!node.children.containsKey(c)) {
                return word;
            }

            node = node.children.get(c);
        }

        return word;
    }
}

class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        Trie trie = new Trie();
        StringBuilder string = new StringBuilder();

        for (String word: dictionary) {
            trie.insert(word);
        }

        for (String s: sentence.split(" ")) {
            String res = trie.search(s);
            if (string.length() != 0) {
                string.append(" ");
            }
            string.append(res);
        }

        return string.toString();
    }
}
