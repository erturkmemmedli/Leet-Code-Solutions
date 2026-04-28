class Solution:
    def evaluate(self, expression: str) -> int:
        tokens, st, d = [''], [], {}
        
        def calculate(tokens):
            if tokens[0] in ['add', 'mult']:
                n1, n2 = int(d.get(tokens[1], tokens[1])), int(d.get(tokens[2], tokens[2]))
                return str(n1+n2) if tokens[0] == 'add' else str(n1*n2)
            else:
                for i in range(1, len(tokens)-2, 2):
                    d[tokens[i]] = d.get(tokens[i+1], tokens[i+1])
                return d.get(tokens[-1], tokens[-1]) 
            
        for c in expression:
            if c == '(':
                if tokens[0] == 'let':
                    calculate(tokens)
                st.append((tokens, dict(d)))
                tokens = ['']
                # print('case 1:','stack:',st,'tokens:',tokens,'dict:',d)
            elif c == ')':
                val = calculate(tokens)
                tokens, d = st.pop()
                tokens[-1] += val
                # print('case 2:','stack:',st,'tokens:',tokens,'dict:',d)
            elif c == ' ':
                tokens.append('')
                # print('case 3:','stack:',st,'tokens:',tokens,'dict:',d)
            else:
                tokens[-1] += c
                # print('case 4:','stack:',st,'tokens:',tokens,'dict:',d)

        return int(tokens[0])
