class Solution {
    public String toGoatLatin(String sentence) {
        String[] words = sentence.split(" ");
        StringBuilder converted = new StringBuilder();
        
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            String rep = repeatChar('a', i + 1);

            if (isVowel(Character.toLowerCase(word.charAt(0)))) {
                converted.append(word).append("ma").append(rep);
            } else {
                String second = word.substring(1);
                char first = word.charAt(0);
                converted.append(second).append(first).append("ma").append(rep);
            }

            if (i != words.length - 1) {
                converted.append(" ");
            }
        }

        return converted.toString();
    }

    public boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'u' || c == 'i' || c == 'o';
    }

    public String repeatChar(char c, int r) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < r; i++) {
            result.append(c);
        }

        return result.toString();
    }
}
