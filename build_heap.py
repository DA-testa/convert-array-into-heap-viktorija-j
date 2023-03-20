#211RDB250

def sift_down(i, n, data, swaps):
    min_index = i
    left_child = 2 * i + 1
    if left_child < n and data[left_child] < data[min_index]:
        min_index = left_child
    right_child = 2 * i + 2
    if right_child < n and data[right_child] < data[min_index]:
        min_index = right_child
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(min_index, n, data, swaps)

def build_heap(n, data):
    swaps = []
    for i in range(n // 2, -1, -1):
        sift_down(i, n, data, swaps)
    return swaps

if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    swaps = build_heap(n, data)
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])
