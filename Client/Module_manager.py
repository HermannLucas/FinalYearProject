import imp
import os

global status

class PluginLoader():
    def __init__(self):
        self.PluginFolder = "./Client/Modules"
        self.MainModule = "interface"

    def getPlugins(self):
        plugins = []
        possibleplugins = os.listdir(self.PluginFolder)
        for i in possibleplugins:
            location = os.path.join(self.PluginFolder, i)
            if not os.path.isdir(location) or not self.MainModule + ".py" in os.listdir(location):
                continue
            info = imp.find_module(self.MainModule,  [location])
            plugins.append({"name" : i,  "info" : info})
        return plugins
    
    def loadPlugin(self, plugin):
        return imp.load_module(self.MainModule, *plugin["info"])


class Manager:
    def __init__(self):
        self.set_status("Starting")
        self.module_list = {}
        self.pluginmanager = PluginLoader()
        for i in self.pluginmanager.getPlugins():
            print("Loading plugin " + i["name"])
            plugin = self.pluginmanager.loadPlugin(i).run() 
            self.module_list[plugin.name] = plugin
        self.set_status("Wainting")
    
    def execute_order(self, order):
        order.execute()
    
    def list_modules(self):
        names = None
        for module in self.module_list:
            if names is None:
                names = []
            else:
                names.append("--|--")
            names.append("{}".format(module))
        return ''.join(names)
    
    def set_status(self, stat):
        global status
        status = stat
    
    def get_status(self):
        return status