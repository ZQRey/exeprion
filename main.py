import math

class MyRange:
    def __init__(self, first, second=None, step=1):
        if second is None:
            self.start = 0
            self.end = first
        else:
            self.start = first
            self.end = second

        if step != 0:
            self.step = step
        else:
            raise ValueError('Step cannot be zero!')

        self.lenght = math.ceil((self.end - self.start) / self.step)

    def __len__(self):
        return self.lenght

    def __getitem__(self, item):
        if 0 <= item < len(self):
            return self.start + item * self.step
        else:
            raise IndexError('MyRange index out of range.')

    def __repr__(self):
        return 'MyRange({}, {}, {})'.format(self.start, self.end, self.step)


r = MyRange(100000, 10, -1)
for _ in r:
    print(_)