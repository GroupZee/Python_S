class bookname:
    def start(self):
        print("book is starting....")
    def stop(self):
        print("book is stopping....")
a=bookname()
a.start()
a.stop()

class isbat:
    o="hello"
    def __init__(self,name):
        self.name = name
    @classmethod
    def sample(cls):
        return cls.o
print(isbat.sample())        