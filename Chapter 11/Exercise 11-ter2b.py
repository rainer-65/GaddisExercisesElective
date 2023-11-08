class First(object):
    def __init__(self):
        print("First(): entering")
        super().__init__()
        print("First(): exiting")


class Second(object):
    def __init__(self):
        print("Second(): entering")
        print("Second(): exiting")


class Third(First, Second):
    def __init__(self):
        print("Third(): entering")
        super().__init__()
        print("Third(): exiting")


Third()
