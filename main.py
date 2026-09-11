class HashTable:
    def __init__(self) -> None:
        self.collection = {}

    def hash(self, key: str) -> int:
        return sum(ord(i) for i in list(key))

    def add(self, key: str, value: int | float | str) -> None:
        index = self.hash(key)
        if index in self.collection:
            self.collection[index].update({key: value})
        else:
            self.collection[index] = {key: value}

    def remove(self, key):
        pass

    def lookup(self, key):
        pass
    

x = HashTable()
x.add('ab', 'ab')
x.add('ba', 'ba')
x.add('coma', 'coma')
print(x.collection)
