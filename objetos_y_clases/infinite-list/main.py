class InfiniteList:
    def __init__(self, *items, fill_value=None):
        self.items = list(items)
        self.fill_value = fill_value

    def __getitem__(self, index: int):
        return self.items[index]
    
    def __setitem__(self, index: int, value):
        while len(self.items) <= index:
            self.items.append(self.fill_value)
        self.items[index] = value

    def __len__(self):
        return(len(self.items))

    def __str__(self):
        return ','.join(str(value)for value in self.items)
