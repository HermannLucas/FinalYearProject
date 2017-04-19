import socket
import Network_manager
from Interpreter import Prompter
from Head import Order_director
from Client.Module_manager import Manager


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
    def __init__(self, args):
        self.type = "Client"
        if args["Head"]:
            self.order_director = SingletonDecorator(Order_director)
            self.ord_dir = self.order_director()
            self.serv = Network_manager.Reciever_manager(self.ord_dir)
            self.serv.start()
            self.ord_dir.conn_man = self.serv
            self.head = True
        
        self.module_manager = SingletonDecorator(Manager)
        self.mod_man = self.module_manager()
        
        if "name" in args:
            self.name = args["name"]
        else:
            self.name = socket.gethostname()
        
        if "config" in args:
            self.config_path = args["config"]
        else:
            self.config_path = "Path"
        
        if "nameservice" in args:
            self.nameservice = args["nameservice"]
            
        else:
            self.nameservice = "Nameservice"
        
        if args["Shell"]:
            interpreter = Prompter(self)
            interpreter.cmdloop()
        
        if args["connect"]:
            self.clent = Network_manager.Sender_manager(self.name)
