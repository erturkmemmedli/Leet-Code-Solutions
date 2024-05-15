class Solution {
    public int numRookCaptures(char[][] board) {
        List<Integer> rookCoordinate = findRookCoordinate(board);
        List<List<Integer>> directions = Arrays.asList(
            Arrays.asList(0, 1),
            Arrays.asList(1, 0),
            Arrays.asList(0, -1),
            Arrays.asList(-1, 0)
        );
        int captures = 0;

        for (List<Integer> direction: directions) {
            int r = rookCoordinate.get(0);
            int c = rookCoordinate.get(1);
            int x = direction.get(0);
            int y = direction.get(1);

            while (r >= 0 && r < 8 && c >= 0 && c < 8) {
                if (board[r][c] == 'B') {
                    break;
                } else if (board[r][c] == 'p') {
                    captures += 1;
                    break;
                }

                r += x;
                c += y;
            }
        }

        return captures;
    }

    public List<Integer> findRookCoordinate(char[][] board) {
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (board[i][j] == 'R') {
                    return Arrays.asList(i, j);
                }
            }
        }

        return null;
    }
}
