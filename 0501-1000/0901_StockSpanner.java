class StockSpanner {
    private Stack<List<Integer>> stack;

    public StockSpanner() {
        this.stack = new Stack<>();
    }
    
    public int next(int price) {
        int count = 1;

        while (!stack.empty() && stack.peek().get(0)<=price) {
            count += stack.pop().get(1);
        }

        stack.push(List.of(price, count));
        return count;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */
