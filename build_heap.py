#211RDB250

def heapify(i, data):
    parent = (i - 1) // 2

    if i == 2 and len(data) == 3:
        parent = 0

    if parent < 0:
        return 0

    if data[i] < data[parent]:
        print(parent, i)
        data[i], data[parent] = data[parent], data[i]
        return 1 + heapify(parent, data)

    return 0


def build_heap(data):
    n = len(data)
    swaps = []

    for i in range(n // 2, -1, -1):
        for j in range(heapify(i, data)):
            swaps.append((i, (i - 1) // 2))

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
