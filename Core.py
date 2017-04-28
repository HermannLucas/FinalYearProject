import socket
import threading
from Network_manager import ThreadedTCPServer, ThreadedTCPRequestHandler, Client
from Interpreter import Prompter
from Head import Order_director
from Client.Module_manager import Manager
from Client.Serv import Nameserv_putter

class Order:
    pass

class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None
    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance

class Starter:
    def __init__(self, args):
<<<<<<< HEAD
        HOST, PORT = "localhost", 1050

=======
        self.type = "Client"
        if args["Head"]:
            self.order_director = SingletonDecorator(Order_director)
            self.ord_dir = self.order_director()
            self.head = True
        
        self.module_manager = SingletonDecorator(Manager)
        self.mod_man = self.module_manager()
        putter = Nameserv_putter(self.mod_man)
        putter.run()
        
>>>>>>> 073ad5a7bbed3a6de19eec662174d030475dda9e
        if "name" in args:
            self.name = args["name"]
        else:
            self.name = socket.gethostname()
        
        module_manager = SingletonDecorator(Manager)
        mod_man = module_manager(self.name)
        
        if args["Head"]:
            order_director = SingletonDecorator(Order_director)
            ord_dir = order_director()
            server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
            server.name = self.name
            server_thread = threading.Thread(target = server.serve_forever)
            server_thread .daemon = True
            server_thread.start()
            ord_dir.server = server
        else:
            client = Client(mod_man)
            conn = client.connect(HOST, PORT, self.name)
            print(conn)
            client.listen(conn[0], conn[1])
            
        mod_man.head = ord_dir
        
    
        
        if "config" in args:
            self.config_path = args["config"]
        else:
            self.config_path = "Path"
        
        if "nameservice" in args:
            self.nameservice = args["nameservice"]
            
        else:
            self.nameservice = "Nameservice"
        
        if args["Shell"]:
            interpreter = Prompter()
            interpreter.server = server
            interpreter.ord_dir = ord_dir
            interpreter.mod_man = mod_man
            interpreter.cmdloop()
