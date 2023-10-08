  class Range:
    def __init__(self, start=0, stop=None, step=1):
        if not stop:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        if step == 0:
            raise ValueError(f'{self.__class__.__name__}() arg 3 must not be zero')
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        raise StopIteration

    def __repr__(self):
        return f'{self.__class__.__name__}({self.start}, {self.stop}{", " + str(self.step) if self.step > 1 else ""})'


print(Range(2, 11, 3))
print(list(Range(2, 11, 3)))

print(range(2, 11, 3))
print(list(range(2, 11, 3)))

r = Range(2, 11, 3)
r = iter(r)
print(next(r))
print(next(r))
print(next(r))
