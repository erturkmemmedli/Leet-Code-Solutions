class Tuple {
    String word;
    int count;

    public Tuple(String word, int count) {
        this.word = word;
        this.count = count;
    }
}

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

    public void search(Queue<Tuple> queue, String word, int count) {
        Node node = this.root;
        
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);

            if (!node.children.containsKey(c)) {
                return;
            }

            node = node.children.get(c);
            
            if (node.isEnd) {
                queue.add(new Tuple(word.substring(i + 1), count + 1));
            }
        }
    }
}

class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Trie trie = new Trie();
        List<String> output = new ArrayList<>();
        Queue<Tuple> queue;
        HashSet<String> visited;

        for (String word: words) {
            trie.insert(word);
        }

        for (String word: words) {
            queue = new LinkedList<>();
            queue.add(new Tuple(word, 0));
            visited = new HashSet<>();

            while (!queue.isEmpty()) {
                Tuple tuple = queue.remove();

                if (tuple.word.equals("")) {
                    if (tuple.count > 1) {
                        output.add(word);
                        break;
                    }
                    continue;
                }

                if (!visited.contains(tuple.word)) {
                    visited.add(tuple.word);
                    trie.search(queue, tuple.word, tuple.count);
                }
            }
        }

        return output;
    }
}
