class Solution {
    public String defangIPaddr(String address) {
        StringBuilder result = new StringBuilder();

        for (int i=0; i<address.length(); i++) {
            char c = address.charAt(i);
            if (c != '.') result.append(c);
            else result.append("[.]");
        }

        return result.toString();
    }
}
