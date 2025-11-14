class Memoize(object):

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not args in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]
