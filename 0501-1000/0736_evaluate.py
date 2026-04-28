class Solution:
    def evaluate(self, expression: str) -> int:
        stack = []
        tokens = ['']
        dictionary = {}

        def calculate(tokens):
            if tokens[0] in ['add', 'mult']:
                v1 = int(dictionary.get(tokens[1], tokens[1]))
                v2 = int(dictionary.get(tokens[2], tokens[2]))
                return str(v1+v2) if tokens[0] == 'add' else str(v1*v2)
            else:
                for i in range(1, len(tokens)-2, 2):
                    dictionary[tokens[i]] = dictionary.get(tokens[i+1], tokens[i+1])
                return dictionary.get(tokens[-1], tokens[-1])
        
        for char in expression:
            if char == '(':
                if tokens[0] == 'let':
                    calculate(tokens)
                stack.append([tokens, dict(dictionary)])
                tokens = ['']
                # print('case 1:','stack:',st,'tokens:',tokens,'dict:',d)
            elif char == ')':
                result = calculate(tokens)
                tokens, dictionary = stack.pop()
                tokens[-1] += result
                # print('case 2:','stack:',st,'tokens:',tokens,'dict:',d)
            elif char == ' ':
                tokens.append('')
                # print('case 3:','stack:',st,'tokens:',tokens,'dict:',d)
            else:
                tokens[-1] += char
                # print('case 4:','stack:',st,'tokens:',tokens,'dict:',d)

        return int(tokens[0])
