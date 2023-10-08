def reversePattern(row, column):
    if row == 0:
        return

    if row > column:
        print('*', end = " ")
        column += 1
    else:
        print()
        row -= 1
        column = 0

    reversePattern(row, column)

reversePattern(4, 0)

print()

def pattern(row, column):
    if row == 0:
        return

    if row > column:
        column += 1
        pattern(row, column)
        print('*', end = " ")
    else:
        row -= 1
        column = 0
        pattern(row, column)
        print()

pattern(4, 0)