# n = int(input()) + 1
#
# for row in range(1, n):
#     for col in range(1, row + 1):
#         print(col, end='')
#
#     print(*(i for i in range(row - 1, 0, -1)), sep='')


n = int(input()) + 1

for row in range(1, n):
    print(''.join([str(col) for col in range(1, row + 1)]), end='')
    print(*(i for i in range(row - 1, 0, -1)), sep='')
