class Solution:
    def isValid(self, s: str) -> bool: 
        self.stack = []
        self.s = s
        for character in self.s:
            if character in ['(','[','{']:
                self.stack.append(character)
            else:
                if not self.stack:
                    return False
                characterBefore = self.stack.pop()
                if characterBefore == '(':
                    if character != ')':
                        return False
                if characterBefore == '[':
                    if character != ']':
                        return False
                if characterBefore == '{':
                    if character != '}':
                        return False
        if self.stack: 
            return False
        return True
        
