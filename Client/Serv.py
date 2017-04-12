import sys
import socket
from omniORB import CORBA
import CosNaming
from Client.Module_manager import Manager

orb = CORBA.ORB_init(sys.argv,  CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

client = Manager
client_object =client._this()

obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
    print("Failed to narrow the root naming context")
    sys.exit(1)

name = [CosNaming.NameComponent("Context",  "NameService")]
try:
    context = rootContext.bind_new_context(name)
    print("New context bound.")
except CosNaming.NamingContext.AlreadyBound:
    print("Context already exist")
    obj = rootContext.resolve(name)
    context = obj._narrow(CosNaming.NamingContext)
    if context is None:
        print("Context exist but it is not a NamingContext")
        sys.exit(1)

name = [CosNaming.NameComponent(socket.gethostname(), "Client")]
try:
    context.bind(name, client_object)
    print("New Client object bound.")
except CosNaming.NameComponent.AlreadyBound:
    context.rebind(name, client_object)
    print("Client object already existed -- rebound.")

poaManager = poa._get_the_POAmanager
poaManager.activate()

orb.run()
