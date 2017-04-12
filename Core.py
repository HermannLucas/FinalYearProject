class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None
    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance

class Order:
    def execute(self):
        pass

class Starter:
    def __init__(self, *args):
        if "name" in args:
            self.name = args["name"]
        else:
            self.name = socket.gethotsname
        
