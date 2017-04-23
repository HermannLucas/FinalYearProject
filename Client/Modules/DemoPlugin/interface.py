from Client.Module_interface import Abstract_interface, Abstract_Order

class Demo_interface(Abstract_interface):
    
    def __init__(self, mod_man):
        self.name = "Demonstration_plugin"
        self.mod_man = mod_man
    
    @property
    def version(self):
        return "1.0"
    def generate_text(self, arg):
        text = "This is a message from the demo module on the machine called {}".format(self.mod_man.name)
        text += "\n user added text : {}".format(arg)
        text += "\n module : {}".formzt(self.name)
        text += "\n version {}".format(self.version)
        self.display_text(text)
    
    def display_text(self, text):
        print(text)
    
    def demo(self):
        order = Order()
        self.mod_man.send(order)

class Order(Abstract_Order):
    def __init__(self):
        self.module_name = "Demonstration plugin"
    
    def execute(self, module):
        module.generate_text()
        module.display_text()

def begin(mod_man):
    return Demo_interface(mod_man)
