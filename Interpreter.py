from cmd import Cmd

class Prompter(Cmd):
    
    def __init__(self, core):
        self.core = core
        print(self.core)
        super(Prompter, self).__init__()

    intro = "Welcome to my shell.       Type help or ? to list commands.\n"
    prompt = "->"
    
    def do_list_modules(self, arg):
        "List installed modules."
        print(self.core.mod_man.list_modules())
    
    def do_list_clients(self, arg):
        "List all the client managed by this head."
        for client in self.core.ord_dir.client_list:
            print(client)
    
    def do_list_cluster(self, arg):
        "List all the clusters managed by this head."
        for cluster in self.core.ord_dir.cluster_list:
            print(cluster)
    
    def do_list_cluster_clients(self, arg):
        "List all the clients in the selected cluster."
        if arg in self.core.ord_dir.cluster_list:
            self.core.ord_dir.list_client_in_cluster(arg)
    
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
            for client in self.core.ord_dir.client_list:
                self.core.ord_dir.get_client_status(client)
    
    def do_module(self, arg):
        "To intereact with the selected module"
        pass
    
    def do_exit(self, arg):
        "Exit the program."
        print("Bye.")
        return True
    
    
    
#        arg = arg.split(' ')
#        for element in arg:
#            print(element)
#        print("These are your arguments : {}".format(arg))
