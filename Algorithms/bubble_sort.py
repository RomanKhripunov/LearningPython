def bubble_sort(items_list):
    counter = 0
    changed = True
    while changed:
        for ind, item in enumerate(items_list):
            next_val = ""
        main_item = 0
        next_item = 0
        if main_item > next_item:
            main_item, next_item = next_item, main_item


class Some(object):
    def getAttrs(self):
        attrs = []
        for key in self.__dict__:
            attrs.append("%s=%s" % (key, getattr(self, key)))
        return ", ".join(attrs)

    def __str__(self):
        return "[%s: %s]" % (self.__class__.__name__, self.getAttrs())


if __name__ == '__main__':
    class TestSome(Some):
        count = 0

        def __init__(self):
            self.attr1 = TestSome.count
            self.attr2 = TestSome.count + 1
            TestSome.count += 2

    class SubTest(TestSome):
        pass

    Y, X = TestSome(), SubTest()
    print(Y)
    print(X)
