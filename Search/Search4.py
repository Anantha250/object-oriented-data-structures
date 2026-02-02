class Data:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"


class Hash:
    def __init__(self, tSize, maxColl, threShold):
        self.tSize = tSize
        self.maxColl = maxColl
        self.threshold = threShold
        self.duplTable = []
        self.table = [None for _ in range(tSize)]

    def rehashTsize(self, n: int):
        n *= 2
        while True:
            n += 1
            cnt = 0
            for i in range(2, n):
                if n % i == 0:
                    cnt += 1
                    if cnt > 0:
                        break
            if cnt == 0:
                return n

    def rehashResize(self):
        self.tSize = self.rehashTsize(self.tSize)
        self.table = [None for _ in range(self.tSize)]

    def rehashInsert(self):
        old = self.duplTable[:]
        self.duplTable = []
        for v in old:
            bIdx = idx = v % self.tSize
            coll = 0
            while self.table[idx]:
                coll += 1
                print(f"collision number {coll} at {idx}")
                if coll == self.maxColl:
                    break
                idx = (bIdx + coll ** 2) % self.tSize
            if not self.table[idx]:
                self.table[idx] = Data(v)
                self.duplTable.append(v)

    def insert(self, val: int):
        print(f"Add : {val}")
        bIdx = idx = val % self.tSize
        coll = 0
        while self.table[idx]:
            coll += 1
            print(f"collision number {coll} at {idx}")
            if coll == self.maxColl:
                print("****** Max collision - Rehash !!! ******")
                self.rehashResize()
                self.rehashInsert()
                idx = val % self.tSize
                break
            idx = (bIdx + coll ** 2) % self.tSize

        self.duplTable.append(val)
        if len(self.duplTable) * 100 / self.tSize >= self.threshold:
            print("****** Data over threshold - Rehash !!!******")
            self.rehashResize()
            self.rehashInsert()
        else:
            self.table[idx] = Data(val)

    def __str__(self):
        s = ""
        for i, v in enumerate(self.table):
            s += f"#{i+1} {v}\n"
        return s + "----------------------------------------"


def main():
    print(" ***** Rehashing *****")
    inp = input("Enter Input : ").split("/")
    tSize, maxColl, threShold = map(int, inp[0].split())
    h = Hash(tSize, maxColl, threShold)
    print("Initial Table :")
    print(h)
    for x in inp[1].split():
        h.insert(int(x))
        print(h)


if __name__ == "__main__":
    main()
