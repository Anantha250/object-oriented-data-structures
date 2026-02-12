def find_subset(lst, target):
    subsets = [[]]
    for x in lst:
        new = []
        for s in subsets:
            new.append(s + [x])
        subsets += new

    ans = []
    for s in subsets:
        if sum(s) == target:
            ans.append(bubble(s))

    ans = subset_sort(ans)

    if not ans:
        print("No Subset")
    else:
        for s in ans:
            print(s)


def bubble(inp):
    a = inp[:]
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def subset_sort(inp):
    for i in range(len(inp)):
        for j in range(len(inp) - i - 1):
            if compare(inp[j], inp[j + 1]):
                inp[j], inp[j + 1] = inp[j + 1], inp[j]
    return inp


def compare(a, b):
    if len(a) > len(b):
        return True
    if len(a) < len(b):
        return False
    for i in range(len(a)):
        if a[i] > b[i]:
            return True
        if a[i] < b[i]:
            return False
    return False


num, data = input("Enter Input : ").split("/")
num = int(num)
data = list(map(int, data.split()))
find_subset(data, num)
