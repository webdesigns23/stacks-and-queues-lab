def is_valid_parentheses(string):
    stack = []  
    parentheses_pairs = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in parentheses_pairs.values():
            stack.append(char)
        elif char in parentheses_pairs.keys():
            if stack and stack[-1] == parentheses_pairs[char]:
                stack.pop()
            else:
                return False

    return not stack

# Tests
print(is_valid_parentheses("()[]{}")) 
print(is_valid_parentheses(")]}"))  
print(is_valid_parentheses("(({}))"))    