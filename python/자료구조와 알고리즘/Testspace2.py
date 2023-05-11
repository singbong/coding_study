class fibo():
    def __init__(self, x):
        self.x = x

    def finder(self):
        if self.x == 1 or self.x == 2:
            return 1
        return fibo(self.x - 1).finder() + fibo(self.x - 2).finder()

find = fibo(4)
print(find.finder())

