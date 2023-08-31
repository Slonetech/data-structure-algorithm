def is_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:  # If the stack is empty, no opening bracket to match
                return False
            last_opening_bracket = stack.pop()
            if opening_brackets.index(last_opening_bracket) != closing_brackets.index(char):
                return False  # Mismatched brackets
        else:
            continue  # Ignore other characters

    return len(stack) == 0  # If stack is empty, expression is balanced

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
