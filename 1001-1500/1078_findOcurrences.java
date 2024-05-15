class Solution {
    public String[] findOcurrences(String text, String first, String second) {
        String[] words = text.split(" ");
        List<String> resultList = new ArrayList<>();

        for (int i = 0; i < words.length - 2; i++) {
            if (words[i].equals(first) && words[i + 1].equals(second)) {
                resultList.add(words[i + 2]);
            }
        }

        String[] result = new String[resultList.size()];
        result = resultList.toArray(result);

        return result;
    }
}
