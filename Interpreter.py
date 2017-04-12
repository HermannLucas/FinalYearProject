from cmd import Cmd

class Prompter(Cmd):
    intro = "Welcome to my shell.       Type help or ? to list commands.\n"
    prompt = "->"
    
    def do_list_modules(self, arg):
        "List installed modules."
    
    def do_list_clients(self, arg):
        "List all the client managed by this head."
        print("test")
    
    def do_list_cluster(self, arg):
        "List all the clusters managed by this head."
        arg = arg.split(' ')
        for element in arg:
            print(element)
        print("These are your arguments : {}".format(arg))
    
    def do_list_cluster_clients(self, arg):
        "List all the clients in the selected cluster."
        pass
    
    def do_get_client_status(self, arg):
        "Get the status of the selected client(s). If no client's name is inputed, display all the connected client(s) status."
        pass
    
    def do_get_cluster_status(self, arg):
        "Get the status of the selected cluster(s). If no cluster's name is inputed, displays all the connected cluster(s) status."
        pass
    
    def do_module(self, arg):
        "To intereact with the selected module"
        pass
    
    def do_exit(self, arg):
        "Exit the program."
        print("Bye.")
        return True
    
if __name__ == '__main__':
    Prompter().cmdloop()
