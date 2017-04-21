from cmd import Cmd

class Prompter(Cmd):
    
    def __init__(self):
        super(Prompter, self).__init__()

    intro = "Welcome to my shell.       Type help or ? to list commands.\n"
    prompt = "->"
    
    def do_connect_client(self, arg):
        "Connects a new client to this head (<client_name> <client_reference>"
        if arg in self.server.clients:
            client = self.server.clients[arg]
            print(client)
            self.ord_dir.set_client(arg, client)
    
    def do_create_cluster(self, args):
        "Create a new cluster (<clster_name>)"
        args = args.split()
        if len(args) != 1:
            print ("*** invalid number of arguments")
            return
        self.ord_dir.set_cluster(args[0])
    
    def do_add_client_to_cluster(self, args):
        "Add the selected client to the selected cluster (<cluster> <client>)"
        args = args.split()
        if len(args) != 2:
            print("*** Invalid number of arguments")
            return
        self.ord_dir.add_client_in_cluster(args[0], args[1])
    
    def do_list_modules(self, arg):
        "List installed modules."
        print(self.mod_man.list_modules())
    
    def do_list_clients(self, arg):
        "List all the client managed by this head."
        for client in self.ord_dir.client_list:
            print(self.ord_dir.client_list[client].name, self.ord_dir.client_list[client].ref)
    
    def do_list_cluster(self, arg):
        "List all the clusters managed by this head."
        for cluster in self.ord_dir.cluster_list:
            print(cluster)
    
    def do_list_cluster_clients(self, arg):
        "List all the clients in the selected cluster."
        if arg in self.ord_dir.cluster_list:
            for client in self.ord_dir.list_client_in_cluster(arg):
                print(client.name)
    
    def do_get_client_status(self, arg):
        "Get the status of the selected client(s). If no client's name is inputed, display all the connected client(s) status."
        if arg in self.ord_dir.client_list:
            self.ord_dir.get_client_status(arg)
        else:
            for client in self.core.ord_dir.client_list:
                self.core.ord_dir.get_client_status(client)
    
    def do_get_cluster_status(self, arg):
        "Get the status of the selected cluster(s). If no cluster's name is inputed, displays all the connected cluster(s) status."
        if arg in self.ord_dir.cluster_list:
            self.ord_dir.get_cluster_status(arg)
        else:
            for client in self.ord_dir.client_list:
                self.ord_dir.get_client_status(client)
    
    def do_module(self, arg):
        "To intereact with the selected module"
        pass
    
    def do_exit(self, arg):
        "Exit the program."
        self.server.shutdown()
        print("Bye.")
        return True
    
    def do_print(self, arg):
        print(self.server.clients)
    
    def do_send(self, args):
        args = args.split()
        if len(args) != 2:
            print("***Invalid number of arguments")
            return        
        if args[0] in self.ord_dir.client_list:
            self.ord_dir.send(args[0], args[1])
    
    def do_send_cluster(self, args):
        args = args.split()
        if len(args) != 2:
            print("***Invalid number of arguments")
            return
        if args[0] in self.ord_dir.cluster_list:
            self.ord_dir.send_to_cluster(args[0], args[1])
    
#        arg = arg.split(' ')
#        for element in arg:
#            print(element)
#        print("These are your arguments : {}".format(arg))
