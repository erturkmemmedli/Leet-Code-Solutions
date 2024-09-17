class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        HashMap<String, List<String>> recipeGraph = new HashMap<>();
        HashMap<String, Integer> indegree = new HashMap<>();
        Queue<String> queue = new LinkedList<>();
        List<String> output = new ArrayList<>();

        for (int i = 0; i < recipes.length; i++) {
            if (!recipeGraph.containsKey(recipes[i])) {
                recipeGraph.put(recipes[i], new ArrayList<>());
            }
            
            for (String ingredient: ingredients.get(i)) {
                if (!recipeGraph.containsKey(ingredient)) {
                    recipeGraph.put(ingredient, new ArrayList<>());
                }
                recipeGraph.get(ingredient).add(recipes[i]);

                indegree.put(recipes[i], indegree.getOrDefault(recipes[i], 0) + 1);
            }
        }

        for (String supply: supplies) {
            if (recipeGraph.containsKey(supply) ) {
                queue.add(supply);
            }
        }

        while (!queue.isEmpty()) {
            String node = queue.remove();

            if (indegree.containsKey(node)) {
                output.add(node);
            }

            for (String child: recipeGraph.get(node)) {
                indegree.put(child, indegree.get(child) - 1);

                if (indegree.get(child) == 0) {
                    queue.add(child);
                }
            }
        }

        return output;
    }
}
