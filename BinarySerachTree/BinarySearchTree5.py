class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.count = 0
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root

        cur = self.root
        while True:
            if data >= cur.data:
                if cur.right == None:
                    cur.right = Node(data)
                    return cur.right
                else :
                    cur = cur.right
            else:
                if cur.left == None:
                    cur.left = Node(data)
                    return cur.left
                else :
                    cur = cur.left

    def boolean(self, mode, data, sum):
        if mode == 'L':
            return sum < data
        elif mode == 'E':
            return sum == data
        elif mode == 'M':
            return sum > data
        return False
    
    def delete(self, node, parent):
        if node == self.root:
            self.root = None
            
        elif node == parent[-1].left:
            parent[-1].left = None
        elif node == parent[-1].right:
            parent[-1].right = None
    
    def dfs(self, node, parent: list, data, sum, mode):
        if node.left:
            left =  self.dfs(node.left, parent+[node], data, sum+node.data, mode)
        if node.right:
            right = self.dfs(node.right, parent+[node], data, sum+node.data, mode)
        if node.left is None and node.right is None:
            if self.boolean(mode, data, sum+node.data):
                self.delete(node, parent)
                self.print_path(parent+[node])
                return 1
    
    def main_dfs(self, data, mode):
        self.count = 1
        self.dfs(self.root, [], data, 0, mode)
        if self.count == 1:
            print("No paths were removed.")
        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def print_path(self, path: list):
        print(f"{self.count}) {'->'.join([str(e) for e in path])} = {sum([e.data for e in path])}")
        self.count += 1

T = BST()
inp = input('Enter <Create City A (BST)>/<Create conditions and deploy the army>: ').split('/')
for k in inp[0].split():
    T.insert(int(k))
print("(City A) Before the war:")
T.printTree(T.root)
temp = inp[1].split(',')
for i, k in enumerate(temp):
    print("--------------------------------------------------")
    if k[0] == 'L':
        print(f"Removing paths where the sum is less than {k[2:]}:")
        T.main_dfs(int(k[2:]), 'L')
    elif k[0] == 'E':
        print(f"Removing paths where the sum is equal to {k[3:]}:")
        T.main_dfs(int(k[3:]), 'E')
    elif k[0] == 'M':
        print(f"Removing paths where the sum is greater than {k[2:]}:")
        T.main_dfs(int(k[2:]), 'M')
    print("--------------------------------------------------")
    print("(City A) After the war:")
    if T.root is None :
        print("City A has fallen!")
        break
    T.printTree(T.root)
        