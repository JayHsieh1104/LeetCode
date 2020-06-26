class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        num_stack = []
        current_string = ""
        string_stack = []
        
        for char in s:
            if char.isdigit():
                num = 10 * num + int(char)
            elif char == '[':
                num_stack.append(num)
                num = 0
                string_stack.append(current_string)
                current_string = ""
            elif char == ']':
                current_string = string_stack.pop() + num_stack.pop() * current_string
            else:
                current_string += char
        
        return current_string