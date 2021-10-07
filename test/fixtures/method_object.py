def add(a, b):
    return NewMethodObject(a, b)()


class NewMethodObject(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a + self.b


def main():
    print(f"{a} + {b} = {a + b}")
