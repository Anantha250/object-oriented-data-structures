def metadrome(s):
    return all(s[i] < s[i+1] for i in range(len(s)-1))

def plaindrome(s):
    return all(s[i] <= s[i+1] for i in range(len(s)-1))

def katadrome(s):
    return all(s[i] > s[i+1] for i in range(len(s)-1))

def nialpdrome(s):
    return all(s[i] >= s[i+1] for i in range(len(s)-1))

def repdrome(s):
    return len(set(s)) == 1


inp = input("Enter Input : ")

if repdrome(inp):
    print("Repdrome")
elif metadrome(inp):
    print("Metadrome")
elif plaindrome(inp):
    print("Plaindrome")
elif katadrome(inp):
    print("Katadrome")
elif nialpdrome(inp):
    print("Nialpdrome")
else:
    print("Nondrome")
