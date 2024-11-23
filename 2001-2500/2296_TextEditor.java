class ListNode {
    char val;
    ListNode prev;
    ListNode next;

    public ListNode(char val) {
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}


class TextEditor {
    ListNode text;
    ListNode cursor;

    public TextEditor() {
        this.text = new ListNode('|');
        this.cursor = text;
    }
    
    public void addText(String text) {
        if (this.cursor.prev != null) {
            ListNode temp = this.cursor.prev;
            for (int i = 0; i < text.length(); i++) {
                char c = text.charAt(i);
                ListNode node = new ListNode(c);
                temp.next = node;
                node.prev = temp;
                temp = temp.next;
            }
            temp.next = this.cursor;
            this.cursor.prev = temp;
        } else {
            ListNode head = new ListNode(text.charAt(0));
            ListNode temp = head;
            for (int i = 1; i < text.length(); i++) {
                char c = text.charAt(i);
                ListNode node = new ListNode(c);
                temp.next = node;
                node.prev = temp;
                temp = temp.next;
            }
            temp.next = this.cursor;
            this.cursor.prev = temp;
            this.text = head;
        }
        // printText();
    }
    
    public int deleteText(int k) {
        int count = 0;
        for (int i = 0; i < k; i++) {
            if (this.cursor.prev != null) {
                this.cursor.prev = this.cursor.prev.prev;
                if (this.cursor.prev != null) {
                    this.cursor.prev.next = this.cursor;
                }
                count++;
            } else {
                break;
            }
        }
        if (this.cursor.prev == null) {
            this.text = this.cursor;
        }
        // printText();
        return count;
    }

    public String cursorLeft(int k) {
        for (int i = 0; i < k; i++) {
            if (this.cursor.prev != null) {
                this.cursor.val = this.cursor.prev.val;
                this.cursor.prev.val = '|';
                this.cursor = this.cursor.prev;
            } else {
                break;
            }
        }
        if (this.cursor.prev == null) {
            this.text = this.cursor;
        }
        // printText();
        return getCharacterUntilCursor();
    }
    
    public String cursorRight(int k) {
        for (int i = 0; i < k; i++) {
            if (this.cursor.next != null) {
                this.cursor.val = this.cursor.next.val;
                this.cursor.next.val = '|';
                this.cursor = this.cursor.next;
            } else {
                break;
            }
        }
        // printText();
        return getCharacterUntilCursor();
    }

    public String getCharacterUntilCursor() {
        StringBuilder result = new StringBuilder();
        ListNode temp = this.cursor.prev;
        while (temp != null && result.length() < 10) {
            result.append(temp.val);
            temp = temp.prev;
        }
        result.reverse();
        return result.toString();
    }

    public void printText() {
        ListNode temp = this.text;
        StringBuilder t = new StringBuilder();
        while (temp != null) {
            t.append(temp.val);
            temp = temp.next;
        }
        System.out.println(t);
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor obj = new TextEditor();
 * obj.addText(text);
 * int param_2 = obj.deleteText(k);
 * String param_3 = obj.cursorLeft(k);
 * String param_4 = obj.cursorRight(k);
 */
