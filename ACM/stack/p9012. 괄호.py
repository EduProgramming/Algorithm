T = int(input())

for t in range(T):
    PS = input()
    result = 'NO'
    close_count = 0
    open_count = 0
    for i in range(len(PS)-1, -1, -1):
        if PS[i] == ')':
            open_count -= 1
            close_count += 1
        else:
            open_count += 1
            close_count -= 1
            if close_count < 0:
                result = 'NO'
                break
    if open_count == 0 and close_count == 0:
        result = 'YES'
    print(result)