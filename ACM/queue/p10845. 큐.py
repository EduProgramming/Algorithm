import sys
input = sys.stdin.readline

N = int(input())

q = []

for i in range(N):
    command = input().split()
    if len(command) > 1:
        command, num = command[0], command[1]
    else:
        command = command[0]

    if command == 'push':
        q.append(num)
    elif command == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif command == 'back':
        if len(q):
            print(q[len(q)-1])
        else:
            print(-1)
    elif command == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif command == 'size':
        print(len(q))
    elif command == 'pop':
        if len(q):
            print(q.pop(0))
        else:
            print(-1)