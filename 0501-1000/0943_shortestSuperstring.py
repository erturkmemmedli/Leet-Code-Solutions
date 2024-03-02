class Solution(object):
    def shortestSuperstring(self, words: List[str]) -> str:
        def distance(src: str, dst: str) -> int:
            # We increase every edge's value by 1 to ensure all edges
            # have positive values.
            for i in range(1, len(src)):
                if dst.startswith(src[i:]):
                    return len(src) - i + 1
            return 1
        
        n = len(words)
        graph = [[1] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                graph[i][j] = distance(words[i], words[j])
                graph[j][i] = distance(words[j], words[i])
                
        dp = [[0] * n for _ in range(1 << n)]
        max_overlap = -1  # Max overlap found so far
        max_path = []  # The corresponding path
        FINAL_MASK = (1 << n) - 1
        
        # BFS.
        # Each item in the queue is (node, mask, path, overlap)
        queue = collections.deque((i, 1<<i, [i], 0) for i in range(n))
        while queue:
            node, mask, path, overlap = queue.popleft()
            # dp[mask][node] might have been updated by other queue items.
            # Skip if the current item is no longer worth considering.
            if dp[mask][node] > overlap:
                continue
            if mask == FINAL_MASK and overlap > max_overlap:
                max_overlap = overlap
                max_path = path
                continue
            for i in range(n):
                if (1 << i) & mask:  # i already visited
                    continue
                next_mask = mask | (1 << i)
                potential_overlap = dp[mask][node] + graph[node][i] 
                if potential_overlap > dp[next_mask][i]:
                    dp[next_mask][i] = potential_overlap
                    queue.append((i, next_mask, path + [i], potential_overlap))
                    
        # Given the path in `max_path`, generate the output
        ans = words[max_path[0]]
        for i in range(1, n):
            prev, cur = max_path[i-1], max_path[i]
            overlap = graph[prev][cur] - 1
            ans += words[cur][overlap:]
            
        return ans

# Alternative solution

class Solution:
    def shortestSuperstring(self, A):
        @lru_cache(None)
        def suff(w1, w2):
            return [w2[i:] for i in range(len(w1) + 1) if w1[-i:] == w2[:i] or not i][-1]
        
        @lru_cache(None)
        def dp(mask, l):
            if mask + 1 == 1<<N: return ""
            return min([suff(A[l], A[i]) + dp(mask | 1<<i, i) for i in range(N) if not mask & 1<<i], key = len)
        
        N = len(A)
        return min([A[i] + dp(1<<i, i) for i in range(N)], key=len)

# Alternative solution (MLE error)

class Solution(object):
    def shortestSuperstring(self, words):
        def getDistance(s1, s2):
            for i in range(1, len(s1)):
                if s2.startswith(s1[i:]):
                    return len(s1) - i
            return 0

        def pathtoStr(words, graph, path):
            res = words[path[0]]
            for i in range(1, len(path)):
                res += words[path[i]][graph[path[i-1]][path[i]]:]
            return res

        n = len(words)
        graph = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                graph[i][j] = getDistance(words[i], words[j])
                graph[j][i] = getDistance(words[j], words[i])

        bitmask = [[0]*n for _ in range(1<<n)]
        queue = collections.deque([(i, 1<<i, [i], 0) for i in range(n)])
        length = -1
        path_result = []
        
        while queue:
            node, mask, path, distance = queue.popleft()
            if distance < bitmask[mask][node]: continue
            if mask == (1<<n) - 1 and distance > length:
                path_result, length = path, distance
                continue

            for i in range(n):
                new_mask = mask | (1<<i)
                if new_mask != mask and bitmask[mask][node] + graph[node][i] >= bitmask[new_mask][i]:
                    bitmask[new_mask][i] = bitmask[mask][node] + graph[node][i]
                    queue.append((i, new_mask, path+[i], bitmask[new_mask][i]))

        return pathtoStr(words,graph,path_result)
