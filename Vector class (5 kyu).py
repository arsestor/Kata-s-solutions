class Vector():
    def __init__(self, c):
        self.c = c
    def add(self, v):
        return v([self.c[i]+v.c[i] for i in range(len(self.c))])
    def subtract(self, v):
        return v([self.c[i]-v.c[i] for i in range(len(self.c))])
    def dot(self, v):
        return sum([self.c[i]*v.c[i] for i in range(len(self.c))])
    def norm(self):
        return sum([i**2 for i in self.c])**0.5
    def __str__(self):
        return ''.join(str(tuple(self.c)).split())
    def equals(self, v):
        if len(self.c) == len(v.c):
            for i in range(len(self.c)):
                if self.c[i] != v.c[i]:
                    return False
            return True
        else:
            return False
