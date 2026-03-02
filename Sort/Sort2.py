inp = list(map(int, input("Enter list of numbers: ").split()))

freq = {}
first_index = {}

for idx, value in enumerate(inp):
    if value not in freq:
        freq[value] = 0
        first_index[value] = idx
    freq[value] += 1

sorted_items = sorted(freq.keys(), key=lambda x: (-freq[x], first_index[x]))

for num in sorted_items:
    print(f'number {num}, total: {freq[num]}')