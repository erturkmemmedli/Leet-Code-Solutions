class Solution {
    public void solve(char[][] board) {
        int m = board.length, n = board[0].length;
        HashSet<String> set = new HashSet<>();
        Queue<int[]> queue = new LinkedList<>();
        int[][] directions = {{-1,0},{1,0},{0,-1},{0,1}};

        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') {
                set.add(i + ",0");
                queue.add(new int[] {i, 0});
            }
            if (board[i][n-1] == 'O') {
                set.add(i + "," + String.valueOf(n-1));
                queue.add(new int[] {i, n-1});
            }
        }

        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O') {
                set.add("0," + j);
                queue.add(new int[] {0, j});
            }
            if (board[m-1][j] == 'O') {
                set.add(String.valueOf(m-1) + "," + j);
                queue.add(new int[] {m-1, j});
            }
        }

        while (!queue.isEmpty()) {
            int[] node = queue.remove();
            int x = node[0], y = node[1];
            for (int[] dir: directions) {
                int r = x+dir[0], c = y+dir[1];
                if (r>=0 && r<m && c>=0 && c<n && !set.contains(r+","+c) && board[r][c]=='O') {
                    set.add(r + "," + c);
                    queue.add(new int[] {r, c});
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!set.contains(i + "," + j)) {
                    board[i][j] = 'X';
                }
            }
        }
    }
}

// Alternative solution

class Solution {
    public void solve(char[][] board) {
        int m = board.length, n = board[0].length;        
        Queue<int[]> queue = new LinkedList<>();
        int[][] directions = {{-1,0},{1,0},{0,-1},{0,1}};

        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') {
                board[i][0] = '*';
                queue.add(new int[] {i, 0});
            }
            if (board[i][n-1] == 'O') {
                board[i][n-1] = '*';
                queue.add(new int[] {i, n-1});
            }
        }

        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O') {
                board[0][j] = '*';
                queue.add(new int[] {0, j});
            }
            if (board[m-1][j] == 'O') {
                board[m-1][j] = '*';
                queue.add(new int[] {m-1, j});
            }
        }

        while (!queue.isEmpty()) {
            int[] node = queue.remove();
            int x = node[0], y = node[1];
            for (int[] dir: directions) {
                int r = x+dir[0], c = y+dir[1];
                if (r>=0 && r<m && c>=0 && c<n && board[r][c]!='*' && board[r][c]=='O') {
                    board[r][c] = '*';
                    queue.add(new int[] {r, c});
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if (board[i][j] == '*') {
                    board[i][j] = 'O';
                } 
            }
        }
    }
}
