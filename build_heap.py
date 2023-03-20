#211RDB250

def biuld_heap(i, data):
    parent = (i//2) - 1
    if i == 3:
        parent = 1

    if parent < 0:
        return

    if data[i] < data[parent]:
        # swap parent and child
        print(parent, i)
        data[i], data[parent] = data[parent], data[i]
        biuld_heap(parent, data)

def main():
    inp = input()
    if inp == "I":
        n = int(input())
        data = list(map(int, input().split()))
    elif inp == "F":
        print("F")
        return

    assert len(data) == n

    leaves = list(range(n//2, n))
    print("leaves =", leaves, "\n")

    for k in leaves[::-1]:
        biuld_heap(k, data)

    # output how many swaps were made
    # this number should be less than 4n (less than 4*len(data))
    print(1)

if __name__ == "__main__":
    main()

