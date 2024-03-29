class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {supply: [] for supply in supplies}
        in_degree = {supply: 0 for supply in supplies}

        for i, ingredientList in enumerate(ingredients):
            for ingredient in ingredientList:
                if ingredient not in graph:
                    graph[ingredient] = []
                graph[ingredient].append(recipes[i])
                in_degree[recipes[i]] = in_degree.get(recipes[i], 0) + 1

        queue = deque(supplies)
        output = []

        while queue:
            supply = queue.popleft()
            if supply in graph:
                for ingredient in graph[supply]:
                    in_degree[ingredient] -= 1
                    if in_degree[ingredient] == 0:
                        output.append(ingredient)
                        queue.append(ingredient)
        
        return output

# Alternative solution

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # construct directed graph, direction from ingredients to recipes
        # construct indegree to determine whether recipe is reached
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
                indegree[recipe] += 1

        queue = deque(supplies)
        result_list = []

        while queue:
            supply = queue.popleft()

            if supply in graph:
                for recipe in graph[supply]:
                    indegree[recipe] -= 1

                    if indegree[recipe] == 0:
                        result_list.append(recipe)
                        queue.append(recipe)

        return result_list
