# Created by matthewkight at 5/9/22


def isValid(s: str) -> bool:
    stack = []
    incomming = {'{' : '}', '(' : ')', '[' : ']'}
    outgoing = {'}', ')', ']'}

    for char in s:
        if char in incomming:
            stack.append(char)
        elif char in outgoing:
            if len(stack) == 0:
                return False

            if incomming[stack[-1]] == char:
                # They match
                stack.pop()
            else:
                # we have found a mismatch
                return False
    # If you make it here then no mismatch found
    return len(stack) == 0


if __name__ == '__main__':
    # Should be true
    print(isValid("()[]{}"))