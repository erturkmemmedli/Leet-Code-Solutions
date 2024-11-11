class Solution {
    public String alienOrder(String[] words) {
        HashMap<Character, List<Character>> graph = new HashMap<>();
        HashMap<Character, Integer> indegree = new HashMap<>();
        Queue<Character> queue = new LinkedList<>();
        StringBuilder order = new StringBuilder();
        
        for (String word: words) {
            for (int i = 0; i < word.length(); i++) {
                indegree.put(word.charAt(i), 0);
            }
        }
        
        for (int i = 1; i < words.length; i++) {
            int j = 0;
            int k = 0;
            boolean found = false;
            
            while (j < words[i-1].length() && k < words[i].length()) {
                char s = words[i-1].charAt(j);
                char t = words[i].charAt(k);
                
                if (s != t) {
                    if (!graph.containsKey(s)) {
                        graph.put(s, new ArrayList<>());
                    }
                    graph.get(s).add(t);
                    indegree.put(t, indegree.get(t) + 1);
                    found = true;
                    break;
                } else {
                    j++;
                    k++;
                }
            }
            
            if (!found && words[i-1].length() > words[i].length()) {
                return "";
            }
        }
        
        indegree.forEach((key, val) -> {
            if (val == 0) {
                queue.add(key);
            }
        });
        
        while (!queue.isEmpty()) {
            char node = queue.remove();
            order.append(node);
            
            if (graph.containsKey(node)) {
                for (char child: graph.get(node)) {
                    indegree.put(child, indegree.get(child) - 1);
                    
                    if (indegree.get(child) == 0) {
                        queue.add(child);
                    }
                }
            }
        }
        
        return (indegree.size() != order.length()) ? "" : order.toString();
    }
}
