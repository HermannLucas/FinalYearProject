import argparse
import socket

parser = argparse.ArgumentParser(description = "Start the package manager on this machine.")

parser.add_argument("-t", "--type", choices = ["head", "client"], required = True, help = "Starts either as Head or Client")
parser.add_argument("-c", "--config", nargs = 1, help = "Start using a precise configuration file", metavar = "Path to config file")
parser.add_argument("-n", "--name", nargs = 1, help = "Specify the name of this machine", metavar = "Client name")
parser.add_argument("-ns", "--nameService", nargs = 1,  help = "To use a different NameService than the one in the configuration file.", metavar = "Nameservice addresse")

args = parser.parse_args()

if args.type == "head":
    print("Starting as Head.")
else:
    print("Starting as client.")

if args.config:
    print("You want to use this file : {}".format(args.config))

if args.name:
    my_name = args.name
else:
    my_name = socket.gethostname()

if args.nameService:
    ns = args.nameService
else:
    pass
    
print(my_name)
