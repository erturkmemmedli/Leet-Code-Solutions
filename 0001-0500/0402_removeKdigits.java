class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Character> stack = new Stack<>();
        String result = "";

        for (int i=0; i<num.length(); i++) {
            while (k > 0 && !stack.empty() && stack.peek() > num.charAt(i)) {
                stack.pop();
                k--;
            }
            stack.push(num.charAt(i));
        }

        while (k > 0) {
            stack.pop();
            k--;
        }

        for (char c: stack) {
            result += (result.isEmpty() && c == '0') ? "" : c; 
        }

        return (result.isEmpty()) ? "0" : result;
    }
}

// Alternative solution

class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Character> stack = new Stack<>();
        String result = "";

        for (int i=0; i<num.length(); i++) {
            while (k > 0 && !stack.empty() && stack.peek() > num.charAt(i)) {
                stack.pop();
                k--;
            }
            stack.push(num.charAt(i));
        }

        while (k > 0) {
            stack.pop();
            k--;
        }

        String s = stack.stream().map(x -> x.toString()).collect(Collectors.joining("")).replaceFirst("^0+", "");
        return (s.isEmpty()) ? "0" : s;
    }
}

// Alternative solution

class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Character> stack = new Stack<>();
        StringBuilder result = new StringBuilder();

        if (num.length() == k) {
            return "0";
        }

        for (int i=0; i<num.length(); i++) {
            while (k > 0 && !stack.empty() && stack.peek() > num.charAt(i)) {
                stack.pop();
                k--;
            }
            stack.push(num.charAt(i));
        }

        while (k > 0) {
            stack.pop();
            k--;
        }

        while (!stack.empty()) {
            result.append(stack.pop());
        }

        result.reverse();
        
        while (result.length() > 1) {
            if (result.charAt(0) == '0') {
                result.deleteCharAt(0);
            } else {
                break;
            }
        }
        
        return result.toString();
    }
}
