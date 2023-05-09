class Set :
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def display(self, msg):
        print(msg, self.items)

    def contains(self, item):
        return item in self.items

    def insert(self, item):
        if item in self.items : return
        for idx in range(len(self.items)) :
            if item > self.items[idx] :
                self.items.append(item)
                return
        self.items.append(item)

    def delete(self, item):
        if item in self.items:
            self.items.remove(item)

    def __eq__(self, setB):
        if self.size() != setB.size() : return False
        for idx in range(len(self.items)):
            if setB.items[idx] != self.items[idx]:
                return False
        return True

    def union(self, setB):
        newset = Set()
        idxa = idxb= 0
        while idxa < self.size() and idxb < setB.size():
            if self.items[idxa] < setB.items[idxb] :
                newset.items.append(self.items[idxa])
                idxa += 1
            elif self.items[idxa] > setB.items[idxb] :
                newset.items.append(setB.items[idxb])
                idxb += 1
            else :
                newset.items.append(self.items[idxa])
                idxa += 1
                idxb += 1
        while idxa < self.size():
            newset.items.append(self.items[idxa])
            idxa += 1
        while idxb < setB.size():
            newset.items.append(setB.items[idxb])
            idxb += 1
        return newset


