#211RDB250

def heapify(data, n, i, swaps):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and data[l] < data[smallest]:
        smallest = l

    if r < n and data[r] < data[smallest]:
        smallest = r

    if smallest != i:
        swaps.append((i, smallest))
        data[i], data[smallest] = data[smallest], data[i]
        heapify(data, n, smallest, swaps)


def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, swaps)
    return swaps


def main():

    input_type = input("I or F: ")
    if "I" in input_type:
        n = int(input())
        data = list(map(int, input().split()))


    elif "F" in input_type:
        filename = input("File name: ")
        with open("tests/"+filename, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    assert len(data) == n
    swaps = build_heap(data)
    print("")
    print(len(swaps))

    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
