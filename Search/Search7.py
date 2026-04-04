from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        self.goto = [{}]
        self.out = defaultdict(list)
        self.fail = {}

    def add_word(self, word):
        curr = 0
        for char in word:
            if char not in self.goto[curr]:
                self.goto.append({})
                self.goto[curr][char] = len(self.goto) - 1
            curr = self.goto[curr][char]
        self.out[curr].append(word)

    def build(self):
        queue = deque()
        for char, node in self.goto[0].items():
            self.fail[node] = 0
            queue.append(node)
        
        while queue:
            curr = queue.popleft()
            for char, next_node in self.goto[curr].items():
                queue.append(next_node)
                fail_node = self.fail.get(curr, 0)
                
                while fail_node > 0 and char not in self.goto[fail_node]:
                    fail_node = self.fail.get(fail_node, 0)
                
                self.fail[next_node] = self.goto[fail_node].get(char, 0)
                
                if self.out[self.fail[next_node]]:
                    self.out[next_node].extend(self.out[self.fail[next_node]])

    def search(self, text):
        curr = 0
        results = defaultdict(list)
        
        for i, char in enumerate(text):
            while curr > 0 and char not in self.goto[curr]:
                curr = self.fail.get(curr, 0)
            
            curr = self.goto[curr].get(char, 0)
            
            if self.out[curr]:
                for word in self.out[curr]:
                    results[word].append(i - len(word) + 1)
                    
        return dict(results)

if __name__ == "__main__":
    ac = AhoCorasick()
    
    keywords = ["he", "she", "his", "hers", "hack", "acker"]
    for kw in keywords:
        ac.add_word(kw)
        
    ac.build()
    
    log_text = "ushershackeris"
    found_threats = ac.search(log_text)
    
    for word, indices in found_threats.items():
        print(f"'{word}': {indices}")