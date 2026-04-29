MOUSE_TURN = 0
CAT_TURN = 1

DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)

        result_map = {}
        for i in range(1, n):
            result_map[(0, i, CAT_TURN)] = result_map[(0, i, MOUSE_TURN)] = MOUSE_WIN
            result_map[(i, i, CAT_TURN)] = result_map[(i, i, MOUSE_TURN)] = CAT_WIN

        outdegree = {}
        for mouse in range(1, n):
            for cat in range(1, n):
                outdegree[(mouse, cat, MOUSE_TURN)] = len(graph[mouse])
                outdegree[(mouse, cat, CAT_TURN)] = len(graph[cat]) - int(0 in graph[cat])

        queue = deque([state for state in result_map.keys()])
        while queue:
            mouse, cat, turn = queue.popleft()
            curr_result = result_map[(mouse, cat, turn)]

            if turn == MOUSE_TURN:
                previous_states = [(mouse, prev_cat, CAT_TURN) for prev_cat in graph[cat]]
            else:
                previous_states = [(prev_mouse, cat, MOUSE_TURN) for prev_mouse in graph[mouse]]

            for prev_state in previous_states:
                if prev_state in result_map:
                    continue
                
                prev_mouse, prev_cat, prev_turn = prev_state
                if prev_cat == 0:
                    continue

                outdegree[prev_state] -= 1
                is_won = (
                    (curr_result == MOUSE_WIN and prev_turn == MOUSE_TURN)
                    or
                    (curr_result == CAT_WIN and prev_turn == CAT_TURN)
                )

                if is_won or outdegree[prev_state] == 0:
                    result_map[prev_state] = curr_result
                    queue.append(prev_state)

        return result_map.get((1, 2, MOUSE_TURN), DRAW)
