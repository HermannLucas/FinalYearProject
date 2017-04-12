class Order_director:
    def __init__(self):
        self.cluster_list = {}
        self.client_list = {}
    
    def set_client(self, name, ref):
        if name not in self.client_list:
            client = Client(name, ref)
            self.client_list[name] = client
            return client
        else:
            print("A client  named {} already exists.".format(name))
            return self.client_list[name]
    
    def del_client(self, name):
        if name in self.client_list:
            for cluster in self.cluster_list:
                if self.client_list[name] in cluster.client_list:
                    cluster.del_client(self.client_list[name])
            del self.client_list[name]

    def set_cluster(self, name):
        if name not in self.cluster_list:
            cluster = Cluster(name)
            self.cluster_list [name] = cluster
            return cluster
        else:
            print("A cluster is alreday named {}".format(name))
            return self.get_cluster(name)
    
    def add_client_in_cluster(self, cluster, client_name):
        if cluster in self.cluster_list:
            if client_name in self.client_list:
                self.cluster_list[cluster].add_client(self.client_list[client_name])
            else:
                print("You must set the client before adding it to a cluster.")
    
    def del_client_in_cluster(self, cluster, client_name):
        if cluster in self.cluster_list:
            if client_name in self.client_list:
                self.cluster_list[cluster].del_client(self.client_list[client_name])
            else:
                print("The client {} doesn't exists.".format(client_name))
    
    def list_client_in_cluster(self, cluster):
        if cluster in self.cluster_list:
            return self.cluster_list[cluster].client_list

    def del_cluster(self, cluster):
        if cluster in self.cluster_list:
            del self.cluster_list[cluster]
        else:
            print("The cluster {} doesn't exists.".format(cluster))
    
    def send(self, client_name, order):
        for client in self.client_list:
            if client_name == self.client_list[client].name:
                print("Sending to : " + self.client_list[client].ref + " order : " + order)
    
    def send_to_cluster(self, cluster_name, order):
        if cluster_name in self.cluster_list:
            self.cluster_list[cluster_name].send(order)

class Cluster:
    def __init__(self, name):
        self.name = name
        self.client_list = []
    
    def add_client(self, client):
        if client not in self.client_list:
            self.client_list.append(client)
        else:
            print("The client {} is alreday in this cluster.".format(client.name))
    
    def del_client(self, client):
        if client in self.client_list:
            self.client_list.remove(client)
        else:
            print("The client {} is not in this cluster.".format(client.name))
    
    def send(self, order):
        for client_name in self.client_list:
            print("Sending to : " + self.client_list[client_name].ref + " order : " + order)

class Client:
    def __init__(self, name, ref):
        self.name = name
        self.ref = ref

