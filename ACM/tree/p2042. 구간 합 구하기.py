import sys
input = sys.stdin.readline

N, M , K = map(int, input().split())
MIN_NUM = -2 ** 63
MAX_NUM = 2 ** 63 - 1

k = 0
while N > 2 ** k:
    k += 1

tree_size = 2 ** (k+1)
tree = [0 for _ in range(tree_size)]

# Create Leaf Node
data_start_idx = tree_size // 2
for i in range(N):
    tree[data_start_idx + i] = int(input())

# Create Tree(Parent) Node
temp_start_idx = data_start_idx
temp_cnt = tree_size // 4
while temp_cnt > 0:
    parent_idx = temp_start_idx // 2
    for i in range(temp_cnt):
        tree[parent_idx + i] = tree[temp_start_idx + 2*i] + tree[temp_start_idx+1 + 2*i]
    temp_cnt = temp_cnt // 2
    temp_start_idx = temp_start_idx // 2

for i in range(M + K):
    a, b, c = map(int, input().split())

    start_index = data_start_idx + b - 1
    if a == 1:
        tree[start_index] = c
        parent_idx = start_index // 2
        while parent_idx >= 1:
            left_child_idx = parent_idx * 2
            right_child_idx = left_child_idx + 1
            tree[parent_idx] = tree[left_child_idx] + tree[right_child_idx]
            parent_idx = parent_idx // 2
    else:
        end_index = data_start_idx + c - 1
        pocket = []
        while end_index >= start_index:
            if start_index % 2:
                pocket.append(tree[start_index])
            if not end_index % 2:
                pocket.append(tree[end_index])
            start_index = (start_index + 1) // 2
            end_index = (end_index - 1) // 2

        prefix_sum = sum(pocket)
        if prefix_sum > MAX_NUM:
            prefix_sum = MAX_NUM
        elif prefix_sum < MIN_NUM:
            prefix_sum = MIN_NUM
        print(prefix_sum)