parenthesis = {
  '}': '{',
  ')': '(',
  ']': '['
}

closingParenthesis = [')', '}', ']']

expr = "[()]{}{[()()]()}"
stack = []
flag = False

for char in expr:
    if char in closingParenthesis:
        if parenthesis[char] != stack[len(stack)-1]:
            flag = True
            break
        stack.pop()
    else:
        stack.append(char)


if flag or len(stack) > 0:
    print("Not balanced")
else:
    print("Balanced")