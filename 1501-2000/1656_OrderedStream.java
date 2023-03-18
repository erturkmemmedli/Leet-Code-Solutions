class OrderedStream {
    private String[] list;
    private int pointer = 0;

    public OrderedStream(int n) {
        list = new String[n];
    }
    
    public List<String> insert(int idKey, String value) {

        list[idKey - 1] = value;

        List<String> strings = new ArrayList<>();

        while (list[pointer] != null) {
            strings.add(list[pointer]);
            pointer++;
            
            if (pointer == list.length) {
                break;
            }
        }

        return strings;
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = new OrderedStream(n);
 * List<String> param_1 = obj.insert(idKey,value);
 */
