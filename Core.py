import socket
import threading
from Network_manager import ThreadedTCPServer, ThreadedTCPRequestHandler, Client
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

class Starter:
    def __init__(self, args):
        HOST, PORT = "localhost", 1050
        if args["Head"]:
            order_director = SingletonDecorator(Order_director)
            ord_dir = order_director()
            server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
            server_thread = threading.Thread(target = server.serve_forever)
            server_thread .daemon = True
            server_thread.start()
            ord_dir.server = server
        
        module_manager = SingletonDecorator(Manager)
        mod_man = module_manager()
        
        if "name" in args:
            name = args["name"]
        else:
            name = socket.gethostname()
        
        if "config" in args:
            config_path = args["config"]
        else:
            config_path = "Path"
        
        if "nameservice" in args:
            nameservice = args["nameservice"]
            
        else:
            nameservice = "Nameservice"
        
        if args["Shell"]:
            interpreter = Prompter()
            interpreter.server = server
            interpreter.ord_dir = ord_dir
            interpreter.mod_man = mod_man
            interpreter.cmdloop()
        
        if args["connect"]:
            client = Client()
            client.connect(HOST, PORT, name)
