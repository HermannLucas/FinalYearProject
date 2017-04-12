import unittest

from Core import SingletonDecorator 
from Head import Order_director
from Client.Module_manager import Manager

class HeadTestCase(unittest.TestCase):
    def setUp(self):
        self.order_director = SingletonDecorator(Order_director)
        self.ord_dir = self.order_director()
        for i in range(1, 4):
            self.ord_dir.set_cluster("Fake_cluster{}".format(i))
            self.ord_dir.set_client("Fake_client{}".format(i), "Fake_ref{}".format(i))

    def test_is_singleton(self):
        self.assertIs(self.ord_dir, self.order_director())
    
    def test_create_cluster(self):
        cluster = self.ord_dir.set_cluster("cluster_test")
        self.assertIn("cluster_test", self.ord_dir.cluster_list)
        self.assertIs(cluster, self.ord_dir.cluster_list["cluster_test"])
    
    def test_retrieving_cluster(self):
        cluster = self.ord_dir.set_cluster("cluster_test")
        self.assertIs(cluster, self.ord_dir.cluster_list["cluster_test"])
    
    def test_create_client(self):
        client = self.ord_dir.set_client("client_test", ("ref_test"))
        self.assertIn("client_test", self.ord_dir.client_list)
        self.assertIs(client, self.ord_dir.client_list["client_test"])
    
    def test_retrieving_client(self):
        client = self.ord_dir.set_client("client_test", ("ref_test"))
        self.assertIs(client, self.ord_dir.client_list["client_test"])
    
    def tearDown(self):
        del self.ord_dir
        del self.order_director
    
class Cluster_test_case(unittest.TestCase):
    def setUp(self):
        self.order_director = SingletonDecorator(Order_director)
        self.ord_dir = self.order_director()
        for i in range(1, 4):
            self.ord_dir.set_cluster("Fake_cluster{}".format(i))
            self.ord_dir.set_client("Fake_client{}".format(i), "Fake_ref{}".format(i))
    
    def test_add_client(self):
        self.ord_dir.add_client_in_cluster("Fake_cluster1", "Fake_client1")
        self.assertIn(self.ord_dir.client_list["Fake_client1"], self.ord_dir.list_client_in_cluster("Fake_cluster1"))
    
    def test_remove_client(self):
        for i in range(1, 4):
            self.ord_dir.add_client_in_cluster("Fake_cluster1", "Fake_client{}".format(i))
        self.assertIn(self.ord_dir.client_list["Fake_client1"], self.ord_dir.list_client_in_cluster("Fake_cluster1"))
        self.ord_dir.del_client_in_cluster("Fake_cluster1", "Fake_client1")
        self.assertNotIn(self.ord_dir.client_list["Fake_client1"], self.ord_dir.list_client_in_cluster("Fake_cluster1"))
    
    def tearDown(self):
        del self.ord_dir
        del self.order_director

if __name__ == '__main__':
    unittest.main()

#mod_man = SingletonDecorator(Manager)
#cluster = odr_dir.get_cluster("test")
#odr_dir.set_client("Fake",  "Fake ref")
#for i in range(0, 10) :
#    client = odr_dir.set_client("client{}".format(i), "client{} ref".format(i))
#    cluster.add_client(client.name, client)
#for client in cluster.client_list:
#    print(client)
#
#for client in odr_dir.client_list:
#    print("Client {} is the object : {}.".format(client, odr_dir.client_list[client]))
#cluster = odr_dir.get_cluster("test")
#cluster2 = odr_dir.set_cluster("Fun")
#for i in range(1, 6):
#    client = odr_dir.set_client("Fun man{}".format(i), "Funny dick reference {}".format(i))
#    cluster2.add_client(client.name, client)
#for clus in odr_dir.cluster_list:
#    print("Clients in the cluster {}".format(clus))
#    clusty = odr_dir.get_cluster(clus)
#    for client in clusty.client_list:
#        print("\t Client {} is the object : {}.".format(client, clusty.client_list[client]))
#odr_dir.send("Fake",  "fake order")
#odr_dir.send_to_cluster("test", "fake cluster order")
#
#
#print("\n \n Starting test of the module manager.")
#mod_man = Manager()
#for module in mod_man.module_list:
#    print("Module {} is the object : {}".format(module, mod_man.module_list[module]))
#if "Fake plugin" in mod_man.module_list:
#    print("Module {} the vesion is : {}".format(mod_man.module_list["Fake plugin"].name, mod_man.module_list["Fake plugin"].version))
#print(mod_man.list_modules().split('--|--'))
