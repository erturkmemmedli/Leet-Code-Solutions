class Solution {
    public int[][] directions = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
    
    public char[][] updateBoard(char[][] board, int[] click) {
        int m = board.length, n = board[0].length;
        int x = click[0], y = click[1];

        if (board[x][y] == 'M') {
            board[x][y] = 'X';
            return board;
        } else {
            dfs(board, m, n, x, y);
            return board;
        }
    }

    public void dfs(char[][] board, int m, int n, int x, int y) {
        int count = 0;
        int row;
        int col;

        for (int[] direction: directions) {
            row = x + direction[0];
            col = y + direction[1];
            if (row >= 0 && row < m && col >= 0 && col < n && board[row][col] == 'M') {
                count++;
            }
        }

        if (count > 0) {
            board[x][y] = (char) (count + '0');
            return;
        } 

        board[x][y] = 'B';

        for (int[] direction: directions) {
            row = x + direction[0];
            col = y + direction[1];
            if (row >= 0 && row < m && col >= 0 && col < n && board[row][col] == 'E') {
                dfs(board, m, n, row, col);
            }
        }
    }
}
