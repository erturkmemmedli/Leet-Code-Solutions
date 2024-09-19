class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Arrays.sort(products);
        int n = products.length;
        List<List<String>> output = new ArrayList<>();
        int start = 0;
        int index = 1;

        while (start < n && index <= searchWord.length()) {
            String s = products[start];
            if (!s.substring(0, Math.min(index, s.length())).equals(searchWord.substring(0, index))) {
                start++;
            } else {
                List<String> suggest = new ArrayList<>();
                suggest.add(s);

                if (start + 1 < n) {
                    String s1 = products[start + 1];
                    if (s1.substring(0, Math.min(index, s1.length())).equals(searchWord.substring(0, index))) {
                        suggest.add(s1);
                    }
                }
                if (start + 2 < n) {
                    String s2 = products[start + 2];
                    if (s2.substring(0, Math.min(index, s2.length())).equals(searchWord.substring(0, index))) {
                        suggest.add(s2);
                    }
                }
                output.add(suggest);
                index++;
            }
        }

        int l = output.size();

        for (int i = 0; i < searchWord.length() - l; i++) {
            output.add(new ArrayList<>());
        }

        return output;
    }
}

// Alternative solution

class TrieNode {
    HashMap<Character, TrieNode> children;
    List<String> suggestions;
    boolean isEnd;

    public TrieNode() {
        this.children = new HashMap<>();
        this.suggestions = new ArrayList<>();
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
            if (node.suggestions.size() < 3) {
                node.suggestions.add(word);
            }
        }

        node.isEnd = true;
    }
    
}

class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Arrays.sort(products);
        Trie trie = new Trie();
        
        for (String product: products) {
            trie.insert(product);
        }

        List<List<String>> suggestions = new ArrayList<>();
        TrieNode node = trie.root;

        for (int i = 0; i < searchWord.length(); i++) {
            char c = searchWord.charAt(i);
            if (node != null && node.children.containsKey(c)) {
                node = node.children.get(c);
                suggestions.add(node.suggestions);
            } else {
                node = null;
                suggestions.add(new ArrayList<>());
            }
        }

        return suggestions;
    }
}
