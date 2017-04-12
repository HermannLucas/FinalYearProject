import argparse
from Core import Starter

parser = argparse.ArgumentParser(description = "Start the package manager on this machine.")

parser.add_argument("-t", "--type", choices = ["head", "client"], required = True, help = "Starts either as Head or Client")
parser.add_argument("-c", "--config", nargs = 1, help = "Start using a precise configuration file", metavar = "Path to config file")
parser.add_argument("-n", "--name", nargs = 1, help = "Specify the name of this machine", metavar = "Client name")
parser.add_argument("-ns", "--nameService", nargs = 1,  help = "To use a different NameService than the one in the configuration file.", metavar = "Nameservice addresse")

args = parser.parse_args()

init_args = {}
if args.type == "head":
    init_args["type"] = "Head"
else:
    init_args["type"] = "Client"

if args.config:
    init_args["config"] = args.config

if args.name:
    init_args["name"] = args.name

if args.nameService:
    init_args["nameservice"] = args.nameService

Starter(init_args)
